<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/field-reliability-console-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="./assets/field-reliability-console-light.svg">
  <img src="./assets/field-reliability-console-light.svg" alt="NV Field Reliability Console: a sensor-to-field signal path with diagnostics and rollback" width="100%">
</picture>

# Nicolás Vásquez Yáñez

**Embedded Systems & Industrial IoT Developer**<br>
Viña del Mar, Chile · ESP32 · STM32 · FreeRTOS · LoRaWAN · RS485/Modbus · OTA + rollback

> **Firmware built for the part after the demo.**

I design embedded systems that move from board bring-up to reliable field deployment - with deterministic control, industrial connectivity, diagnostics, and recovery paths built in from the start.

[Explore selected systems](#selected-systems) · [See how I engineer reliability](#reliability-in-practice) · [LinkedIn](https://www.linkedin.com/in/nicol%C3%A1s-v%C3%A1squez-y%C3%A1%C3%B1ez-9b8684151/) · [Upwork](https://www.upwork.com/freelancers/~01cc5ecb54a0f95fcc?viewMode=1) · [Leer en español](./README.es.md)

## Field proof

- **Across firmware and hardware:** from early prototypes and PCB integration to validation, commissioning, and field-oriented hardening.
- **End-to-end embedded work:** MCU firmware, RTOS architecture, industrial signals, wired and wireless links, board bring-up, and diagnostics.
- **Systems made for real constraints:** noisy signals, limited power, intermittent connectivity, remote maintenance, and safe recovery.

My work is strongest where firmware meets physical reality: sensors, control electronics, communications, power behavior, and the operational details that decide whether a device keeps working after deployment.

## Selected systems

### SAT / EWARS early-warning systems

**Context:** connectivity, real-time monitoring, and operational field deployment for early-warning systems.<br>
**Engineering territory:** embedded acquisition, control hardware, telemetry, field integration, and commissioning.<br>
**Public evidence:** [connectivity and monitoring demonstration](https://www.youtube.com/watch?v=atfTgxQO1dA) and [operational deployment at Colbún](https://www.youtube.com/watch?v=G301dtDWlcg).

These projects represent the kind of system-level work I value most: translating environmental signals into dependable information and actionable alerts.

### ESP32 LoRaWAN Industrial Node

**Problem:** collect a 4-20 mA industrial signal and transmit compact telemetry from a power-conscious remote node.<br>
**Architecture:** ESP32 + ADS1115 + LoRa-E5 modem over UART, binary payload encoding, then deep sleep.<br>
**Constraint:** balance measurement quality, payload size, radio activity, and energy use.<br>
**Evidence:** [source and documentation](https://github.com/dev-nicolasv/esp32-lorawan-industrial-node) · [v1.0.0 release](https://github.com/dev-nicolasv/esp32-lorawan-industrial-node/releases/tag/release-pro-v1.0.0).

### ESP32 Robust OTA Architecture

**Problem:** update firmware without allowing network work to compromise critical control behavior.<br>
**Architecture:** isolated FreeRTOS tasks, HTTPS download, SHA-256 validation, dual OTA partitions, watchdog-aware execution, and rollback protection.<br>
**Constraint:** keep the control path deterministic while update and recovery logic run independently.<br>
**Evidence:** [public reference architecture](https://github.com/dev-nicolasv/esp32-robust-ota-architecture). Its validation documentation and license definition are being expanded before any production-ready or open-source claim.

<details>
<summary><strong>More public field work</strong></summary>

- [Cloud seeding system](https://youtu.be/6tkjbmUdPcM)
- [PCB Levix Lite](https://youtu.be/EI487dh6bS8)
- [Musical swing project](https://youtu.be/dYeEN-3rE7M)

</details>

## Reliability in practice

| Engineering layer | What I design for |
| --- | --- |
| **Safe boot and updates** | Firmware validation, dual partitions, bounded update flows, rollback, and explicit failure states |
| **Deterministic runtime** | Isolated tasks, state machines, watchdog strategy, bounded retries, and predictable control paths |
| **Industrial interfaces** | 4-20 mA, 0-10 V, ADC acquisition, RS485, Modbus RTU, relays, and digital I/O |
| **Diagnostics and recovery** | Useful logs, status payloads, error classification, remote recovery paths, and maintainable field behavior |

**Core platforms:** ESP32, STM32, C/C++, FreeRTOS, ESP-IDF, PlatformIO, LoRaWAN, MQTT, WiFi, BLE, UART, SPI, I2C, CAN, XBee/DigiMesh, Altium Designer, and KiCad.

## Public engineering lab

- **[esp32-lorawan-industrial-node](https://github.com/dev-nicolasv/esp32-lorawan-industrial-node)** - a low-power industrial telemetry reference built around 4-20 mA acquisition and LoRaWAN uplink.
- **[esp32-robust-ota-architecture](https://github.com/dev-nicolasv/esp32-robust-ota-architecture)** - a public reference for separating critical control, download, validation, and recovery concerns; its license is still pending.

Project descriptions in this profile are intentionally static and readable. The important information does not depend on third-party stat cards, counters, or live image services.

## Now and beyond engineering

I am especially interested in industrial monitoring, early-warning systems, remote telemetry, safe OTA, RS485/Modbus gateways, battery or solar-powered nodes, and products that need to move from unstable prototype to maintainable deployment.

<details>
<summary><strong>Mentorship, workshops, and the human side</strong></summary>

I care about teaching robotics and making low-level engineering more approachable. [Watch a public workshop excerpt](https://youtu.be/h6abCMyFRaY).

Faith is also part of how I approach responsibility, service, and long-term work. I trust in God, and I try to let that conviction show through consistency rather than slogans.

</details>

## Contact

I am open to embedded and Industrial IoT collaborations where a prototype needs stronger architecture, hardware integration, diagnostics, or a credible path to field deployment.

- [Connect on LinkedIn](https://www.linkedin.com/in/nicol%C3%A1s-v%C3%A1squez-y%C3%A1%C3%B1ez-9b8684151/)
- [Discuss a project on Upwork](https://www.upwork.com/freelancers/~01cc5ecb54a0f95fcc?viewMode=1)
- [Explore my GitHub work](https://github.com/dev-nicolasv)

**Build it. Validate it. Deploy it. Keep it running.**
