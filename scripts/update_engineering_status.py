#!/usr/bin/env python3
"""Generate the Field Ops / Live SVG from public GitHub repository metadata.

The updater deliberately uses only Python's standard library and public
``api.github.com`` endpoints.  Fixture mode is completely offline so the
renderer can be tested without consuming API quota.

The output is assembled and validated in memory, then installed with an
atomic rename.  A network, schema, or rendering error therefore leaves the
last valid SVG untouched.
"""

from __future__ import annotations

import argparse
import html
import json
import os
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
import re
import sys
import tempfile
from typing import Any, Mapping, Sequence
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen
import xml.etree.ElementTree as ET


API_ROOT = "https://api.github.com"
API_VERSION = "2022-11-28"
USER_AGENT = "dev-nicolasv-field-ops-status/1.0"
DEFAULT_OUTPUT = Path("assets/live/engineering-status.svg")


@dataclass(frozen=True)
class RepositoryConfig:
    slug: str
    display_name: str
    classification: str
    signal_path: str
    accent: str


@dataclass(frozen=True)
class RepositorySnapshot:
    config: RepositoryConfig
    workflow_status: str
    release_label: str
    license_label: str
    updated_at: datetime


REPOSITORIES: tuple[RepositoryConfig, ...] = (
    RepositoryConfig(
        slug="dev-nicolasv/esp32-lorawan-industrial-node",
        display_name="LORAWAN INDUSTRIAL NODE",
        classification="FIELD NODE",
        signal_path="4-20 mA  ->  ADC  ->  ESP32  ->  LoRaWAN",
        accent="#22D3EE",
    ),
    RepositoryConfig(
        slug="dev-nicolasv/esp32-robust-ota-architecture",
        display_name="ROBUST OTA ARCHITECTURE",
        classification="REFERENCE",
        signal_path="CONTROL  ||  UPDATE  ->  SHA-256  ->  A/B  ->  ROLLBACK",
        accent="#F59E0B",
    ),
)

FAILED_CONCLUSIONS = {
    "action_required",
    "cancelled",
    "failure",
    "startup_failure",
    "timed_out",
}
SUCCESS_CONCLUSIONS = {"success"}
MONTHS = (
    "JAN",
    "FEB",
    "MAR",
    "APR",
    "MAY",
    "JUN",
    "JUL",
    "AUG",
    "SEP",
    "OCT",
    "NOV",
    "DEC",
)


class StatusUpdateError(RuntimeError):
    """A safe, user-facing updater failure."""


def _parse_github_time(value: Any, *, field: str) -> datetime:
    if not isinstance(value, str) or not value:
        raise StatusUpdateError(f"GitHub response is missing {field}")
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise StatusUpdateError(f"GitHub returned an invalid {field}") from exc
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc)


def _fixture_name(slug: str, resource: str) -> str:
    return f"{slug.replace('/', '__')}__{resource}.json"


def _read_fixture(
    fixture_dir: Path, slug: str, resource: str, *, optional: bool
) -> Mapping[str, Any] | None:
    fixture_path = fixture_dir / _fixture_name(slug, resource)
    if not fixture_path.is_file():
        if optional:
            return None
        raise StatusUpdateError(f"Required fixture is missing: {fixture_path.name}")
    try:
        value = json.loads(fixture_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise StatusUpdateError(f"Could not read fixture: {fixture_path.name}") from exc
    if not isinstance(value, dict):
        raise StatusUpdateError(f"Fixture must contain a JSON object: {fixture_path.name}")
    return value


def _fetch_public_json(
    path: str, *, query: Mapping[str, str] | None = None, optional: bool = False
) -> Mapping[str, Any] | None:
    # Keeping API_ROOT fixed prevents fixture or CLI input from redirecting the
    # updater (and any future credentials) to a non-GitHub host.
    url = f"{API_ROOT}{path}"
    if query:
        url = f"{url}?{urlencode(query)}"
    request = Request(
        url,
        headers={
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": API_VERSION,
            "User-Agent": USER_AGENT,
        },
    )
    try:
        with urlopen(request, timeout=20) as response:  # noqa: S310 - fixed host
            payload = json.load(response)
    except HTTPError as exc:
        if optional and exc.code == 404:
            return None
        if exc.code in {403, 429}:
            raise StatusUpdateError(
                "GitHub API rate limit reached; preserving the previous SVG"
            ) from exc
        raise StatusUpdateError(
            f"GitHub API request failed with HTTP {exc.code}: {path}"
        ) from exc
    except (URLError, TimeoutError, OSError, json.JSONDecodeError) as exc:
        raise StatusUpdateError(
            f"GitHub API request failed; preserving the previous SVG: {path}"
        ) from exc
    if not isinstance(payload, dict):
        raise StatusUpdateError(f"GitHub returned an unexpected payload: {path}")
    return payload


def _resource(
    config: RepositoryConfig,
    resource: str,
    *,
    fixture_dir: Path | None,
    default_branch: str | None = None,
    optional: bool = False,
) -> Mapping[str, Any] | None:
    if fixture_dir is not None:
        return _read_fixture(fixture_dir, config.slug, resource, optional=optional)

    endpoint = f"/repos/{config.slug}"
    query: Mapping[str, str] | None = None
    if resource == "actions_runs":
        endpoint += "/actions/runs"
        query = {
            "branch": default_branch or "main",
            "per_page": "50",
            "status": "completed",
        }
    elif resource == "latest_release":
        endpoint += "/releases/latest"
    elif resource != "repo":
        raise StatusUpdateError(f"Unknown GitHub resource: {resource}")
    return _fetch_public_json(endpoint, query=query, optional=optional)


def _workflow_summary(payload: Mapping[str, Any], default_branch: str) -> str:
    raw_runs = payload.get("workflow_runs")
    if not isinstance(raw_runs, list):
        raise StatusUpdateError("GitHub actions response is missing workflow_runs")

    completed: list[Mapping[str, Any]] = []
    for value in raw_runs:
        if not isinstance(value, dict):
            continue
        if value.get("status") != "completed":
            continue
        branch = value.get("head_branch")
        if branch not in {None, default_branch}:
            continue
        completed.append(value)

    if not completed:
        return "NO DATA"

    def run_time(run: Mapping[str, Any]) -> datetime:
        candidate = run.get("run_started_at") or run.get("created_at")
        return _parse_github_time(candidate, field="workflow run timestamp")

    latest_per_workflow: dict[str, Mapping[str, Any]] = {}
    for run in sorted(completed, key=run_time, reverse=True):
        workflow_key = str(run.get("workflow_id") or run.get("name") or "workflow")
        latest_per_workflow.setdefault(workflow_key, run)

    conclusions = {
        str(run.get("conclusion") or "").lower()
        for run in latest_per_workflow.values()
    }
    if conclusions & FAILED_CONCLUSIONS:
        return "ATTENTION"
    if conclusions and conclusions <= SUCCESS_CONCLUSIONS:
        return "PASS"
    return "CHECK"


def _license_label(payload: Mapping[str, Any]) -> str:
    license_info = payload.get("license")
    if not isinstance(license_info, dict):
        return "LICENSE PENDING"
    value = license_info.get("spdx_id") or license_info.get("name")
    if not isinstance(value, str) or value.upper() in {"", "NOASSERTION", "OTHER"}:
        return "LICENSE PENDING"
    return _safe_text(value.upper(), maximum=24)


def _release_label(payload: Mapping[str, Any] | None) -> str:
    if payload is None:
        return "NO RELEASE"
    value = payload.get("tag_name")
    if not isinstance(value, str) or not value.strip():
        return "NO RELEASE"
    return _safe_text(value, maximum=30)


def _safe_text(value: str, *, maximum: int) -> str:
    normalized = re.sub(r"\s+", " ", value).strip()
    normalized = "".join(
        character for character in normalized if character.isprintable()
    )
    if len(normalized) > maximum:
        normalized = f"{normalized[: maximum - 1]}…"
    return html.escape(normalized, quote=True)


def collect_snapshot(
    config: RepositoryConfig, *, fixture_dir: Path | None = None
) -> RepositorySnapshot:
    repo = _resource(config, "repo", fixture_dir=fixture_dir)
    if repo is None:  # pragma: no cover - repo is a required resource
        raise StatusUpdateError(f"No repository metadata returned for {config.slug}")

    default_branch = repo.get("default_branch")
    if not isinstance(default_branch, str) or not default_branch:
        raise StatusUpdateError(f"Repository is missing default_branch: {config.slug}")

    actions = _resource(
        config,
        "actions_runs",
        fixture_dir=fixture_dir,
        default_branch=default_branch,
    )
    if actions is None:  # pragma: no cover - actions is a required resource
        raise StatusUpdateError(f"No workflow metadata returned for {config.slug}")
    release = _resource(
        config,
        "latest_release",
        fixture_dir=fixture_dir,
        optional=True,
    )

    return RepositorySnapshot(
        config=config,
        workflow_status=_workflow_summary(actions, default_branch),
        release_label=_release_label(release),
        license_label=_license_label(repo),
        updated_at=_parse_github_time(repo.get("updated_at"), field="updated_at"),
    )


def collect_all(*, fixture_dir: Path | None = None) -> tuple[RepositorySnapshot, ...]:
    return tuple(
        collect_snapshot(config, fixture_dir=fixture_dir) for config in REPOSITORIES
    )


def _compact_date(value: datetime) -> str:
    utc = value.astimezone(timezone.utc)
    return f"{utc.day:02d} {MONTHS[utc.month - 1]} {utc.year}"


def _status_color(status: str) -> str:
    return {
        "PASS": "#2DD4BF",
        "ATTENTION": "#FB7185",
        "CHECK": "#FBBF24",
        "NO DATA": "#94A3B8",
    }[status]


def _pill(x: int, y: int, width: int, label: str, color: str) -> str:
    return (
        f'<g transform="translate({x} {y})">'
        f'<rect width="{width}" height="30" rx="8" fill="{color}" '
        f'fill-opacity="0.11" stroke="{color}" stroke-opacity="0.42"/>'
        f'<text x="14" y="20" class="pill" fill="{color}">{label}</text>'
        "</g>"
    )


def render_svg(
    snapshots: Sequence[RepositorySnapshot], *, generated_at: datetime
) -> str:
    if len(snapshots) != len(REPOSITORIES):
        raise StatusUpdateError("The dashboard requires both repository snapshots")

    sync_time = generated_at.astimezone(timezone.utc)
    rows: list[str] = []
    for index, snapshot in enumerate(snapshots, start=1):
        y = 112 + ((index - 1) * 124)
        status_color = _status_color(snapshot.workflow_status)
        status = _safe_text(snapshot.workflow_status, maximum=16)
        release = _safe_text(snapshot.release_label, maximum=30)
        license_label = _safe_text(snapshot.license_label, maximum=24)
        title = _safe_text(snapshot.config.display_name, maximum=40)
        classification = _safe_text(snapshot.config.classification, maximum=20)
        signal_path = _safe_text(snapshot.config.signal_path, maximum=68)
        accent = snapshot.config.accent

        rows.append(
            f"""
  <g transform="translate(36 {y})">
    <rect width="1128" height="106" rx="16" class="panel"/>
    <rect width="4" height="58" x="0" y="24" rx="2" fill="{accent}"/>
    <text x="28" y="32" class="index" fill="{accent}">0{index}</text>
    <text x="78" y="34" class="title">{title}</text>
    <text x="78" y="61" class="path">{signal_path}</text>
    <text x="1050" y="32" text-anchor="end" class="classify">{classification}</text>
    <text x="1050" y="61" text-anchor="end" class="updated">UPDATED {_compact_date(snapshot.updated_at)}</text>
    {_pill(78, 70, 138, f"CI  {status}", status_color)}
    {_pill(230, 70, 258, f"RELEASE  {release}", accent)}
    {_pill(502, 70, 226, license_label, "#A78BFA")}
    <circle cx="1082" cy="85" r="5" fill="{status_color}" class="pulse-dot"/>
  </g>"""
        )

    sync_label = (
        f"SYNC {sync_time.year:04d}-{sync_time.month:02d}-{sync_time.day:02d} UTC"
    )
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="390" viewBox="0 0 1200 390" role="img" aria-labelledby="title description">
  <title id="title">Field Ops live engineering status</title>
  <desc id="description">Current GitHub workflow, release, and license signals for the LoRaWAN industrial node and robust OTA reference architecture.</desc>
  <defs>
    <linearGradient id="background" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#07131D"/>
      <stop offset="0.62" stop-color="#081722"/>
      <stop offset="1" stop-color="#0B1220"/>
    </linearGradient>
    <pattern id="grid" width="32" height="32" patternUnits="userSpaceOnUse">
      <path d="M 32 0 L 0 0 0 32" fill="none" stroke="#7DD3FC" stroke-opacity="0.035"/>
    </pattern>
  </defs>
  <style>
    text {{ font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; }}
    .eyebrow {{ fill: #67E8F9; font-size: 11px; font-weight: 700; letter-spacing: 2.2px; }}
    .heading {{ fill: #F8FAFC; font-size: 29px; font-weight: 760; letter-spacing: -0.5px; }}
    .sync {{ fill: #94A3B8; font-size: 11px; font-weight: 650; letter-spacing: 1.2px; }}
    .panel {{ fill: #0B1D29; fill-opacity: 0.92; stroke: #244253; stroke-width: 1; }}
    .index {{ font-family: ui-monospace, SFMono-Regular, Menlo, monospace; font-size: 12px; font-weight: 800; letter-spacing: 1px; }}
    .title {{ fill: #E2E8F0; font-size: 16px; font-weight: 760; letter-spacing: 0.7px; }}
    .path {{ fill: #91A4B7; font-family: ui-monospace, SFMono-Regular, Menlo, monospace; font-size: 11px; font-weight: 520; letter-spacing: 0.35px; }}
    .classify {{ fill: #CBD5E1; font-size: 10px; font-weight: 750; letter-spacing: 1.5px; }}
    .updated {{ fill: #64748B; font-size: 9px; font-weight: 650; letter-spacing: 0.75px; }}
    .pill {{ font-family: ui-monospace, SFMono-Regular, Menlo, monospace; font-size: 10px; font-weight: 750; letter-spacing: 0.75px; }}
    .footer {{ fill: #64748B; font-size: 10px; font-weight: 520; letter-spacing: 0.4px; }}
    .pulse-dot {{ animation: pulse 2.4s ease-in-out infinite; transform-box: fill-box; transform-origin: center; }}
    @keyframes pulse {{ 0%, 100% {{ opacity: .45; transform: scale(.8); }} 50% {{ opacity: 1; transform: scale(1.2); }} }}
    @media (prefers-reduced-motion: reduce) {{ .pulse-dot {{ animation: none; }} }}
  </style>
  <rect width="1200" height="390" rx="22" fill="url(#background)"/>
  <rect width="1200" height="390" rx="22" fill="url(#grid)"/>
  <rect x="0.5" y="0.5" width="1199" height="389" rx="21.5" fill="none" stroke="#214153"/>
  <text x="36" y="35" class="eyebrow">DEV-NICOLASV / PUBLIC ENGINEERING SIGNAL</text>
  <text x="36" y="72" class="heading">FIELD OPS / LIVE</text>
  <g transform="translate(900 35)">
    <circle cx="0" cy="-4" r="5" fill="#2DD4BF" class="pulse-dot"/>
    <text x="17" y="0" class="sync">PUBLIC DATA</text>
    <text x="264" y="0" text-anchor="end" class="sync">{sync_label}</text>
  </g>
  <path d="M36 91 H1164" stroke="#244253"/>{''.join(rows)}
  <text x="36" y="374" class="footer">Statuses derived from public GitHub metadata · generated by a bounded repository workflow</text>
</svg>
"""
    validate_svg(svg)
    return svg


def validate_svg(svg: str) -> None:
    lowered = svg.lower()
    forbidden = ("<script", "<foreignobject", "javascript:", "data:text/html")
    if any(token in lowered for token in forbidden):
        raise StatusUpdateError("Generated SVG contains a forbidden construct")
    try:
        root = ET.fromstring(svg)
    except ET.ParseError as exc:
        raise StatusUpdateError("Generated SVG is not valid XML") from exc
    if not root.tag.endswith("svg"):
        raise StatusUpdateError("Generated document is not an SVG")
    if len(svg.encode("utf-8")) > 96_000:
        raise StatusUpdateError("Generated SVG exceeds the safety size limit")


def write_atomic(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary_name: str | None = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            dir=path.parent,
            prefix=f".{path.name}.",
            suffix=".tmp",
            delete=False,
        ) as temporary:
            temporary_name = temporary.name
            temporary.write(content)
            temporary.flush()
            os.fsync(temporary.fileno())
        os.replace(temporary_name, path)
    except OSError as exc:
        raise StatusUpdateError(f"Could not atomically write {path}") from exc
    finally:
        if temporary_name:
            try:
                Path(temporary_name).unlink(missing_ok=True)
            except OSError:
                pass


def _parse_now(value: str | None) -> datetime:
    if value is None:
        return datetime.now(timezone.utc)
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise StatusUpdateError("--now must be an ISO-8601 timestamp") from exc
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT,
        help=f"SVG destination (default: {DEFAULT_OUTPUT})",
    )
    parser.add_argument(
        "--fixture-dir",
        type=Path,
        help="Read deterministic JSON fixtures instead of using the network",
    )
    parser.add_argument(
        "--now",
        help="Override the synchronization time with an ISO-8601 timestamp",
    )
    parser.add_argument(
        "--stdout",
        action="store_true",
        help="Print the SVG without modifying --output",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        fixture_dir = args.fixture_dir.resolve() if args.fixture_dir else None
        snapshots = collect_all(fixture_dir=fixture_dir)
        svg = render_svg(snapshots, generated_at=_parse_now(args.now))
        if args.stdout:
            sys.stdout.write(svg)
        else:
            write_atomic(args.output, svg)
            print(f"Updated {args.output}")
        return 0
    except StatusUpdateError as exc:
        print(f"engineering-status: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
