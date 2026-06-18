# Hi there, I'm Nicolás Vásquez Yáñez 👋

### Senior Embedded Systems & IoT Developer | ESP32 | STM32 | LoRaWAN | Industrial Firmware

Stop paying for fragile prototypes. I build robust, production-ready embedded systems and IoT solutions engineered to thrive in demanding industrial environments.

With over **8 years of end-to-end hardware and firmware experience**, I specialize in taking projects from initial concept to scalable, real-world deployment. I do not just write code; I engineer complete embedded solutions that meet strict industrial constraints.

---

## 🧠 What I Do

I design and develop embedded systems for real-world industrial applications, combining **firmware architecture, hardware integration, field diagnostics, communication protocols, OTA updates, low-power telemetry, and industrial signal acquisition**.

My engineering focus is simple:

> Build embedded systems that keep working when the environment is noisy, remote, constrained, or mission-critical.

---

## 🛠️ Tech Stack, Tools & Industrial Standards

### Firmware & Embedded Systems

![C](https://img.shields.io/badge/C-00599C?style=for-the-badge&logo=c&logoColor=white)
![C++](https://img.shields.io/badge/C++-004482?style=for-the-badge&logo=cplusplus&logoColor=white)
![Espressif](https://img.shields.io/badge/Espressif-E7352C?style=for-the-badge&logo=espressif&logoColor=white)
![ESP32](https://img.shields.io/badge/ESP32-0F172A?style=for-the-badge&logo=espressif&logoColor=white)
![STM32](https://img.shields.io/badge/STM32-03234B?style=for-the-badge&logo=stmicroelectronics&logoColor=white)
![FreeRTOS](https://img.shields.io/badge/FreeRTOS-111827?style=for-the-badge)

### Development Tools

![PlatformIO](https://img.shields.io/badge/PlatformIO-F5822A?style=for-the-badge&logo=platformio&logoColor=white)
![ESP-IDF](https://img.shields.io/badge/ESP--IDF-000000?style=for-the-badge&logo=espressif&logoColor=white)
![STM32CubeIDE](https://img.shields.io/badge/STM32CubeIDE-03234B?style=for-the-badge&logo=stmicroelectronics&logoColor=white)
![VS Code](https://img.shields.io/badge/VS%20Code-007ACC?style=for-the-badge&logo=visualstudiocode&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![Altium Designer](https://img.shields.io/badge/Altium%20Designer-A5915F?style=for-the-badge&logo=altiumdesigner&logoColor=white)

### IoT, RF & Industrial Interfaces

![LoRaWAN](https://img.shields.io/badge/LoRaWAN-6B21A8?style=for-the-badge&logo=thethingsnetwork&logoColor=white)
![MQTT](https://img.shields.io/badge/MQTT-660066?style=for-the-badge&logo=mqtt&logoColor=white)
![WiFi](https://img.shields.io/badge/WiFi-2563EB?style=for-the-badge)
![Bluetooth](https://img.shields.io/badge/Bluetooth-0A66C2?style=for-the-badge&logo=bluetooth&logoColor=white)
![RS485](https://img.shields.io/badge/RS485%20%2F%20Modbus-1E293B?style=for-the-badge)
![UART](https://img.shields.io/badge/UART-334155?style=for-the-badge)
![SPI](https://img.shields.io/badge/SPI-475569?style=for-the-badge)
![I2C](https://img.shields.io/badge/I2C-64748B?style=for-the-badge)
![CAN Bus](https://img.shields.io/badge/CAN%20Bus-0F172A?style=for-the-badge)

---

## ⚙️ Engineering Capabilities

- **Hardware & PCB Design:** Altium Designer for industrial-grade multilayer boards and custom hardware integration.
- **Firmware Architecture:** Modular embedded firmware, RTOS task separation, drivers, state machines, and hardware abstraction layers.
- **IoT & RF Protocols:** LoRaWAN, XBee/DigiMesh, WiFi, Bluetooth, MQTT, and UART-based modem integration.
- **Industrial Interfaces:** RS485, Modbus RTU, UART, SPI, I2C, CAN Bus, digital I/O, relays, and sensor interfaces.
- **Signals & Control:** 4–20 mA, 0–10 V, ADC acquisition, sensor calibration, PID control loops, and low-level hardware troubleshooting.
- **OTA & Reliability:** Secure OTA update flows, watchdog-aware design, rollback protection, firmware validation, and field recovery strategies.
- **Low-Power Systems:** Deep sleep, telemetry cycles, battery-oriented design, compact payloads, and remote sensor autonomy.

---

## 📂 Open-Source Technical Samples

These repositories showcase my coding standards, embedded architecture, RTOS management, and industrial implementation style.

### 📡 [ESP32 LoRaWAN Industrial Node](https://github.com/dev-nicolasv/esp32-lorawan-industrial-node)

Ultra-low power industrial telemetry boilerplate using:

- ESP32
- Seeed LoRa-E5 through UART AT commands
- ADS1115 analog acquisition
- 4–20 mA industrial sensor input
- Compact binary payload encoding
- Deep Sleep optimization

**Architecture:** wake → measure → encode → uplink → sleep.

---

### 🔄 [ESP32 Robust OTA Architecture](https://github.com/dev-nicolasv/esp32-robust-ota-architecture)

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

## 🚀 Featured Industrial & Field Projects

I focus on mission-critical systems where reliability is not optional. Here are some field deployments I have engineered:

| Project | Area | Focus |
|---|---|---|
| 🌊 [Colbún Hydroelectric Early Warning System](https://www.youtube.com/watch?v=atfTgxQO1dA) | Energy / Monitoring | Robust environmental monitoring and alert system for a major energy facility |
| 🚨 [SAT / EWARS Viña del Mar](https://www.youtube.com/watch?v=G301dtDWlcg) | Urban Risk Prevention | Early warning system development for urban disaster prevention |
| ☁️ [Cloud Seeding System — Mettech Seerain](https://youtu.be/6tkjbmUdPcM) | Atmospheric Systems | Complex control hardware for atmospheric weather modification |
| ⚙️ [Custom Hardware & PCB Development](https://youtu.be/EI487dh6bS8) | Hardware Engineering | Complete board design, assembly, and low-level firmware integration |
| 🎵 [Musical Swing — Sergafel](https://youtu.be/dYeEN-3rE7M) | Interactive Hardware | Robust public-use hardware with embedded control and sensing |

---

## 🧩 How I Build Embedded Systems

```mermaid
flowchart LR
    A["Industrial Requirement"] --> B["Hardware Architecture"]
    B --> C["PCB / Hardware Integration"]
    C --> D["Firmware Architecture"]
    D --> E["Driver Layer"]
    E --> F["Protocol Integration"]
    F --> G["Telemetry / Control Logic"]
    G --> H["OTA / Diagnostics"]
    H --> I["Field Validation"]
    I --> J["Scalable Deployment"]
```

I prefer architectures that are:

- **Deterministic** — predictable execution, bounded retries, explicit state machines.
- **Maintainable** — modular drivers, clear configuration, documented interfaces.
- **Field-ready** — watchdogs, recovery paths, diagnostics, and safe OTA.
- **Efficient** — compact payloads, low-power cycles, and minimal runtime overhead.
- **Industrial-aware** — designed for noisy signals, harsh environments, and remote access constraints.

---

## 📊 GitHub Metrics

![Nicolás GitHub Stats](https://github-readme-stats.vercel.app/api?username=dev-nicolasv&show_icons=true&theme=tokyonight&hide_border=true&border_radius=12&include_all_commits=true&count_private=true)

![Top Languages](https://github-readme-stats.vercel.app/api/top-langs/?username=dev-nicolasv&layout=compact&theme=tokyonight&hide_border=true&border_radius=12)

![GitHub Streak](https://streak-stats.demolab.com?user=dev-nicolasv&theme=tokyonight&hide_border=true&border_radius=12)

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

---

## 👨‍🏫 Mentorship & Community

Beyond industrial development, I am passionate about sharing knowledge. I regularly conduct online workshops and teach robotics to kids and teenagers, translating complex low-level engineering concepts into accessible learning experiences.

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

📫 **Reach out to me on [Upwork](https://www.upwork.com/freelancers/~01cc5ecb54a0f95fcc?viewMode=1) or connect with me on [LinkedIn](https://www.linkedin.com/in/nicol%C3%A1s-v%C3%A1squez-y%C3%A1%C3%B1ez-9b8684151/).**

---

## ⚡ Engineering Philosophy

Embedded firmware is not only about making hardware work.

It is about making it keep working in the real world.




