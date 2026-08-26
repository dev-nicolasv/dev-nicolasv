from __future__ import annotations

from datetime import datetime, timezone
import importlib.util
from pathlib import Path
import sys
import tempfile
import unittest
from unittest import mock
import xml.etree.ElementTree as ET


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "update_engineering_status.py"
FIXTURES = Path(__file__).parent / "fixtures" / "engineering_status"

SPEC = importlib.util.spec_from_file_location("update_engineering_status", SCRIPT)
assert SPEC is not None and SPEC.loader is not None
status_module = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = status_module
SPEC.loader.exec_module(status_module)


class EngineeringStatusTests(unittest.TestCase):
    def test_fixture_mode_is_offline_and_policy_labels_are_truthful(self) -> None:
        with mock.patch.object(
            status_module,
            "_fetch_public_json",
            side_effect=AssertionError("network access in fixture mode"),
        ):
            snapshots = status_module.collect_all(fixture_dir=FIXTURES)

        self.assertEqual([item.workflow_status for item in snapshots], ["PASS", "PASS"])
        self.assertEqual(snapshots[0].release_label, "release-pro-v1.0.0")
        self.assertEqual(snapshots[0].license_label, "MIT")
        self.assertEqual(snapshots[1].release_label, "v1.0.0")
        self.assertEqual(snapshots[1].license_label, "LICENSE PENDING")

        svg = status_module.render_svg(
            snapshots,
            generated_at=datetime(2026, 8, 25, 12, 0, tzinfo=timezone.utc),
        )
        root = ET.fromstring(svg)
        self.assertTrue(root.tag.endswith("svg"))
        self.assertIn("REFERENCE", svg)
        self.assertIn("LICENSE PENDING", svg)
        self.assertIn("release-pro-v1.0.0", svg)
        self.assertIn("SYNC 2026-08-25 UTC", svg)
        self.assertNotIn("PRODUCTION", svg.upper())
        self.assertNotIn("<script", svg.lower())
        self.assertNotIn("<foreignobject", svg.lower())

    def test_failed_refresh_preserves_previous_asset(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_dir:
            temporary = Path(temporary_dir)
            output = temporary / "engineering-status.svg"
            output.write_text("last-known-good", encoding="utf-8")
            missing_fixtures = temporary / "missing-fixtures"
            missing_fixtures.mkdir()

            result = status_module.main(
                [
                    "--fixture-dir",
                    str(missing_fixtures),
                    "--output",
                    str(output),
                    "--now",
                    "2026-08-25T12:00:00Z",
                ]
            )

            self.assertEqual(result, 1)
            self.assertEqual(output.read_text(encoding="utf-8"), "last-known-good")

    def test_successful_refresh_writes_valid_svg_atomically(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_dir:
            output = Path(temporary_dir) / "nested" / "engineering-status.svg"
            result = status_module.main(
                [
                    "--fixture-dir",
                    str(FIXTURES),
                    "--output",
                    str(output),
                    "--now",
                    "2026-08-25T12:00:00Z",
                ]
            )

            self.assertEqual(result, 0)
            content = output.read_text(encoding="utf-8")
            ET.fromstring(content)
            self.assertIn("FIELD OPS / LIVE", content)

    def test_latest_completed_run_per_workflow_controls_summary(self) -> None:
        payload = {
            "workflow_runs": [
                {
                    "workflow_id": 1,
                    "head_branch": "main",
                    "status": "completed",
                    "conclusion": "success",
                    "run_started_at": "2026-08-25T12:00:00Z",
                },
                {
                    "workflow_id": 1,
                    "head_branch": "main",
                    "status": "completed",
                    "conclusion": "failure",
                    "run_started_at": "2026-08-24T12:00:00Z",
                },
                {
                    "workflow_id": 2,
                    "head_branch": "main",
                    "status": "completed",
                    "conclusion": "success",
                    "run_started_at": "2026-08-25T11:00:00Z",
                },
            ]
        }
        self.assertEqual(status_module._workflow_summary(payload, "main"), "PASS")


if __name__ == "__main__":
    unittest.main()
