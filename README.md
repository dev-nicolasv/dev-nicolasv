# Hi there, I'm Nicolás Vásquez Yáñez 👋

### Senior Embedded Systems & Industrial IoT Developer  
#### ESP32 | STM32 | LoRaWAN | Firmware Architecture | Hardware Integration | PCB Design

I build **robust embedded systems, industrial IoT devices, and firmware architectures** designed to operate reliably in demanding real-world environments.

With over **8 years of end-to-end hardware and firmware experience**, I specialize in taking projects from concept, prototype, and hardware bring-up to field-ready deployment.

I do not just write code.  
I engineer complete embedded solutions that can survive noise, remote operation, constrained hardware, harsh environments, and strict industrial requirements.

---

## 🚀 What I Build

- Industrial IoT telemetry nodes
- ESP32 and STM32 embedded firmware
- LoRaWAN sensor devices and gateways
- OTA firmware update architectures
- RS485 / Modbus RTU industrial systems
- 4–20 mA and 0–10 V signal acquisition
- Battery and solar-powered embedded devices
- Custom hardware and PCB-integrated firmware
- Field diagnostics and recovery systems
- Prototype rescue and production hardening

> Embedded firmware is not only about making hardware work.  
> It is about making it keep working in the real world.

---

## 🧰 Embedded Technology Stack

### Firmware & Embedded Systems

![C](https://img.shields.io/badge/C-00599C?style=for-the-badge&logo=c&logoColor=white)
![C++](https://img.shields.io/badge/C++-004482?style=for-the-badge&logo=cplusplus&logoColor=white)
![Embedded C](https://img.shields.io/badge/Embedded%20C-1E293B?style=for-the-badge)
![FreeRTOS](https://img.shields.io/badge/FreeRTOS-111827?style=for-the-badge)
![RTOS](https://img.shields.io/badge/RTOS-0F172A?style=for-the-badge)
![State Machines](https://img.shields.io/badge/State%20Machines-334155?style=for-the-badge)

### Microcontrollers & Platforms

![ESP32](https://img.shields.io/badge/ESP32-E7352C?style=for-the-badge&logo=espressif&logoColor=white)
![Espressif](https://img.shields.io/badge/Espressif-000000?style=for-the-badge&logo=espressif&logoColor=white)
![STM32](https://img.shields.io/badge/STM32-03234B?style=for-the-badge&logo=stmicroelectronics&logoColor=white)
![Arduino](https://img.shields.io/badge/Arduino-00979D?style=for-the-badge&logo=arduino&logoColor=white)

### Development Tools

![PlatformIO](https://img.shields.io/badge/PlatformIO-F5822A?style=for-the-badge&logo=platformio&logoColor=white)
![ESP-IDF](https://img.shields.io/badge/ESP--IDF-000000?style=for-the-badge&logo=espressif&logoColor=white)
![STM32CubeIDE](https://img.shields.io/badge/STM32CubeIDE-03234B?style=for-the-badge&logo=stmicroelectronics&logoColor=white)
![VS Code](https://img.shields.io/badge/VS%20Code-007ACC?style=for-the-badge&logo=visualstudiocode&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)

### Hardware & PCB Design

![Altium Designer](https://img.shields.io/badge/Altium%20Designer-A5915F?style=for-the-badge&logo=altiumdesigner&logoColor=white)
![PCB Design](https://img.shields.io/badge/PCB%20Design-166534?style=for-the-badge)
![Hardware Bring-Up](https://img.shields.io/badge/Hardware%20Bring--Up-14532D?style=for-the-badge)
![Multilayer PCB](https://img.shields.io/badge/Multilayer%20PCB-15803D?style=for-the-badge)
![Industrial Hardware](https://img.shields.io/badge/Industrial%20Hardware-166534?style=for-the-badge)

### IoT, RF & Connectivity

![LoRaWAN](https://img.shields.io/badge/LoRaWAN-6B21A8?style=for-the-badge&logo=thethingsnetwork&logoColor=white)
![MQTT](https://img.shields.io/badge/MQTT-660066?style=for-the-badge&logo=mqtt&logoColor=white)
![WiFi](https://img.shields.io/badge/WiFi-2563EB?style=for-the-badge)
![Bluetooth](https://img.shields.io/badge/Bluetooth-0A66C2?style=for-the-badge&logo=bluetooth&logoColor=white)
![XBee](https://img.shields.io/badge/XBee%20%2F%20DigiMesh-F59E0B?style=for-the-badge)
![UART Modems](https://img.shields.io/badge/UART%20Modems-475569?style=for-the-badge)

### Industrial Interfaces & Signals

![RS485](https://img.shields.io/badge/RS485-1E293B?style=for-the-badge)
![Modbus RTU](https://img.shields.io/badge/Modbus%20RTU-334155?style=for-the-badge)
![UART](https://img.shields.io/badge/UART-475569?style=for-the-badge)
![SPI](https://img.shields.io/badge/SPI-64748B?style=for-the-badge)
![I2C](https://img.shields.io/badge/I2C-64748B?style=for-the-badge)
![CAN Bus](https://img.shields.io/badge/CAN%20Bus-0F172A?style=for-the-badge)
![4-20mA](https://img.shields.io/badge/4--20mA-14532D?style=for-the-badge)
![0-10V](https://img.shields.io/badge/0--10V-166534?style=for-the-badge)

---

## 🛡️ Firmware Reliability Matrix

| Area | What I Implement |
|---|---|
| **Boot Safety** | OTA partitions, firmware validation, rollback strategy, safe boot workflows |
| **Runtime Stability** | Watchdogs, bounded retries, deterministic state machines, task isolation |
| **Industrial I/O** | 4–20 mA, 0–10 V, RS485, Modbus RTU, relay control, digital I/O |
| **Connectivity** | LoRaWAN, MQTT, WiFi, BLE, UART modem control, XBee/DigiMesh |
| **Power Strategy** | Deep sleep, telemetry cycles, battery operation, solar-powered systems |
| **Field Diagnostics** | Serial logs, error codes, status payloads, remote recovery paths |
| **Production Readiness** | Versioning, commissioning flow, validation notes, maintainable architecture |
| **Hardware Integration** | PCB bring-up, signal validation, peripheral testing, board-level debugging |

---

## 🧩 Embedded System Architecture

```mermaid
flowchart LR
    A["Industrial Sensor<br/>4-20mA / 0-10V / Digital / RS485"] --> B["Protection & Analog Front-End<br/>Filtering / Scaling / Isolation"]
    B --> C["ADC / MCU Interface<br/>ADS1115 / Internal ADC / GPIO"]
    C --> D["Firmware Core<br/>Drivers / HAL / State Machine"]
    D --> E["Protocol Layer<br/>LoRaWAN / MQTT / Modbus RTU"]
    E --> F["Gateway / Cloud<br/>Telemetry / Alerts / Dashboard"]
    D --> G["OTA Manager<br/>Validation / Rollback / Recovery"]
    D --> H["Power Manager<br/>Deep Sleep / Battery / Solar"]
    D --> I["Diagnostics Layer<br/>Logs / Error Codes / Field Status"]
```

---

## 🚀 From Prototype to Field Deployment

```mermaid
flowchart LR
    A["Concept"] --> B["Hardware Selection"]
    B --> C["Schematic / PCB"]
    C --> D["Firmware Architecture"]
    D --> E["Prototype Bring-Up"]
    E --> F["Field Testing"]
    F --> G["OTA / Diagnostics"]
    G --> H["Production-Ready System"]
```

---

## 📂 Open-Source Technical Samples

These repositories showcase my coding standards, embedded architecture, RTOS management, industrial interfaces, and implementation style.

---

### 📡 ESP32 LoRaWAN Industrial Node

[![ESP32 LoRaWAN Industrial Node](https://github-readme-stats.vercel.app/api/pin/?username=dev-nicolasv&repo=esp32-lorawan-industrial-node&theme=tokyonight&hide_border=true&border_radius=12)](https://github.com/dev-nicolasv/esp32-lorawan-industrial-node)

Ultra-low power industrial telemetry boilerplate using:

- ESP32
- Seeed LoRa-E5 through UART AT commands
- ADS1115 analog acquisition
- 4–20 mA industrial sensor input
- Compact binary payload encoding
- Deep Sleep optimization

**Architecture:** wake → measure → encode → uplink → sleep.

---

### 🔄 ESP32 Robust OTA Architecture

[![ESP32 Robust OTA Architecture](https://github-readme-stats.vercel.app/api/pin/?username=dev-nicolasv&repo=esp32-robust-ota-architecture&theme=tokyonight&hide_border=true&border_radius=12)](https://github.com/dev-nicolasv/esp32-robust-ota-architecture)

Production-oriented OTA firmware architecture featuring:

- FreeRTOS task isolation
- PID control task separation
- HTTPS firmware download
- SHA-256 firmware validation
- Dual OTA partitions
- Watchdog-aware design
- Automatic rollback protection

**Architecture:** keep critical control logic deterministic while OTA runs safely in parallel.

---

## 🏭 Featured Industrial & Field Projects

I focus on mission-critical systems where reliability is not optional.

| Project | Area | Focus |
|---|---|---|
| 🌊 [Colbún Hydroelectric Early Warning System](https://www.youtube.com/watch?v=atfTgxQO1dA) | Energy / Monitoring | Robust environmental monitoring and alert system for a major energy facility |
| 🚨 [SAT / EWARS Viña del Mar](https://www.youtube.com/watch?v=G301dtDWlcg) | Urban Risk Prevention | Early warning system development for urban disaster prevention |
| ☁️ [Cloud Seeding System — Mettech Seerain](https://youtu.be/6tkjbmUdPcM) | Atmospheric Systems | Complex control hardware for atmospheric weather modification |
| ⚙️ [Custom Hardware & PCB Development](https://youtu.be/EI487dh6bS8) | Hardware Engineering | Complete board design, assembly, and low-level firmware integration |
| 🎵 [Musical Swing — Sergafel](https://youtu.be/dYeEN-3rE7M) | Interactive Hardware | Robust public-use hardware with embedded control and sensing |

---

## ⚙️ Engineering Capabilities

### Embedded Firmware

- Modular C/C++ firmware architecture
- ESP32 and STM32 development
- RTOS task separation and scheduling
- Deterministic state machines
- Watchdog-aware design
- Driver development and hardware abstraction
- Serial communication and binary protocols
- Peripheral integration and low-level debugging

### Industrial IoT

- LoRaWAN telemetry nodes
- UART AT modem integration
- MQTT communication
- RS485 and Modbus RTU devices
- Sensor telemetry pipelines
- Remote monitoring systems
- Compact payload encoding
- Cloud and gateway integration

### Hardware & PCB

- Schematic and PCB design support
- Industrial-grade board integration
- Analog signal conditioning
- 4–20 mA and 0–10 V acquisition
- Relay, digital I/O, and power-stage integration
- Hardware bring-up and validation
- Board-level troubleshooting

### Reliability & Field Operation

- OTA firmware update flows
- Rollback-safe firmware deployment
- Runtime fault recovery
- Error reporting and diagnostics
- Low-power telemetry cycles
- Battery and solar operation
- Field commissioning support

---

## 📊 GitHub Metrics

![Nicolás GitHub Stats](https://github-readme-stats.vercel.app/api?username=dev-nicolasv&show_icons=true&theme=tokyonight&hide_border=true&border_radius=12&include_all_commits=true)

![Most Used Languages](https://github-readme-stats.vercel.app/api/top-langs/?username=dev-nicolasv&layout=compact&theme=tokyonight&hide_border=true&border_radius=12&langs_count=8)

---

## 📈 Recent GitHub Activity

![Nicolás GitHub Activity Graph](https://github-readme-activity-graph.vercel.app/graph?username=dev-nicolasv&theme=tokyo-night&hide_border=true&radius=12)

---

## 🧪 Current Areas of Interest

- Industrial LoRaWAN telemetry nodes
- ESP32 OTA update pipelines
- STM32WLE5 / LoRa-E5 modem architectures
- RS485 / Modbus RTU industrial gateways
- Battery and solar-powered IoT systems
- Edge firmware for monitoring and control
- Robust embedded architecture for field deployment
- AI-assisted firmware and PCB workflows
- Industrial monitoring and early warning systems
- Modular IoT hardware for scalable deployments

---

## 👨‍🏫 Mentorship & Community

Beyond industrial development, I am passionate about sharing knowledge.

I regularly conduct online workshops and teach robotics to kids and teenagers, translating complex low-level engineering concepts into accessible learning experiences.

📺 [Watch a snippet of my Online Workshops](https://youtu.be/h6abCMyFRaY)

---

## 🧰 Repository Quality Principles

When I publish technical repositories, I aim to include:

- Clear architecture overview
- Hardware wiring notes
- PlatformIO build instructions
- Industrial use-case explanation
- Payload format documentation
- Commissioning notes
- Security and operational considerations
- Future production-hardening roadmap

---

## 🤝 Let's Work Together

Looking for a senior embedded systems developer to architect your next IoT product, industrial telemetry node, control system, or to rescue a failing prototype?

Let's discuss your technical requirements.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Nicolás%20Vásquez-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/nicol%C3%A1s-v%C3%A1squez-y%C3%A1%C3%B1ez-9b8684151/)
[![Upwork](https://img.shields.io/badge/Upwork-Embedded%20IoT%20Developer-6FDA44?style=for-the-badge&logo=upwork&logoColor=white)](https://www.upwork.com/freelancers/~01cc5ecb54a0f95fcc?viewMode=1)
[![GitHub](https://img.shields.io/badge/GitHub-dev--nicolasv-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/dev-nicolasv)

---

## ⚡ Engineering Philosophy

Embedded systems fail in the details:

- Bad power design
- Noisy signals
- Poor recovery logic
- Weak OTA strategy
- Unclear diagnostics
- Fragile prototypes
- Untested edge cases

My job is to design firmware and hardware integration that anticipates those problems before the product reaches the field.

**Build it. Validate it. Deploy it. Keep it running.**
````
