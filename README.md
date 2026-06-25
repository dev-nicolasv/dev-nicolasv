<p align="center">
  <img src="./assets/embedded-industrial-banner.svg" alt="Nicolás Vásquez Yáñez - Embedded Systems and Industrial IoT" width="100%" />
</p>

# Hi there, I'm Nicolás Vásquez Yáñez 👋

### Senior Embedded Systems & Industrial IoT Developer  
#### ESP32 | STM32 | LoRaWAN | Firmware Architecture | Hardware Integration | PCB Design

I build **robust embedded systems, industrial IoT devices, and production-oriented firmware architectures** designed to operate reliably in demanding real-world environments.

With over **8 years of end-to-end hardware and firmware experience**, I specialize in taking products from concept and prototype to field-ready deployment.

> **Embedded firmware is not only about making hardware work.  
> It is about making it keep working in the real world.**

---

## 🚀 Focus Areas

<table>
<tr>
<td width="33%">

### ⚙️ Firmware

- ESP32 / STM32
- C / C++
- FreeRTOS
- OTA updates
- State machines
- Low-level drivers

</td>
<td width="33%">

### 📡 Industrial IoT

- LoRaWAN
- MQTT
- RS485 / Modbus RTU
- UART modem control
- Remote monitoring
- Field diagnostics

</td>
<td width="33%">

### 🔌 Hardware

- PCB-integrated firmware
- Altium Designer
- KiCad
- 4–20 mA / 0–10 V
- Signal conditioning
- Hardware bring-up

</td>
</tr>
</table>

---

## 🧰 Embedded Technology Stack

<p align="center">
  <img src="https://img.shields.io/badge/C-00599C?style=for-the-badge&logo=c&logoColor=white" />
  <img src="https://img.shields.io/badge/C++-1d4ed8?style=for-the-badge&logo=cplusplus&logoColor=white" />
  <img src="https://img.shields.io/badge/Embedded%20C-1e293b?style=for-the-badge" />
  <img src="https://img.shields.io/badge/FreeRTOS-111827?style=for-the-badge" />
  <img src="https://img.shields.io/badge/RTOS-0f172a?style=for-the-badge" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/ESP32-E7352C?style=for-the-badge&logo=espressif&logoColor=white" />
  <img src="https://img.shields.io/badge/Espressif-111827?style=for-the-badge&logo=espressif&logoColor=white" />
  <img src="https://img.shields.io/badge/STM32-03234B?style=for-the-badge&logo=stmicroelectronics&logoColor=white" />
  <img src="https://img.shields.io/badge/PlatformIO-F5822A?style=for-the-badge&logo=platformio&logoColor=white" />
  <img src="https://img.shields.io/badge/ESP--IDF-000000?style=for-the-badge&logo=espressif&logoColor=white" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Altium%20Designer-6b7280?style=for-the-badge&logo=altiumdesigner&logoColor=white" />
  <img src="https://img.shields.io/badge/KiCad-1d4ed8?style=for-the-badge&logo=kicad&logoColor=white" />
  <img src="https://img.shields.io/badge/PCB%20Design-14532d?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Hardware%20Bring--Up-1f2937?style=for-the-badge" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/LoRaWAN-4c1d95?style=for-the-badge&logo=thethingsnetwork&logoColor=white" />
  <img src="https://img.shields.io/badge/MQTT-581c87?style=for-the-badge&logo=mqtt&logoColor=white" />
  <img src="https://img.shields.io/badge/RS485%20%2F%20Modbus-1e293b?style=for-the-badge" />
  <img src="https://img.shields.io/badge/UART-475569?style=for-the-badge" />
  <img src="https://img.shields.io/badge/SPI-64748b?style=for-the-badge" />
  <img src="https://img.shields.io/badge/I2C-64748b?style=for-the-badge" />
  <img src="https://img.shields.io/badge/CAN%20Bus-0f172a?style=for-the-badge" />
  <img src="https://img.shields.io/badge/4--20mA-14532d?style=for-the-badge" />
  <img src="https://img.shields.io/badge/0--10V-166534?style=for-the-badge" />
</p>

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
| **Hardware Integration** | PCB bring-up, signal validation, peripheral testing, board-level debugging |

---

## 🧩 Embedded System Architecture

```mermaid
flowchart LR
    A["Industrial Sensor"] --> B["Protection & Analog Front-End"]
    B --> C["ADC / MCU Interface"]
    C --> D["Firmware Core"]
    D --> E["Protocol Layer"]
    E --> F["Gateway / Cloud"]
    D --> G["OTA Manager"]
    D --> H["Power Manager"]
    D --> I["Diagnostics Layer"]
```

---

## 📂 Open-Source Technical Samples

<p align="center">
  <a href="https://github.com/dev-nicolasv/esp32-lorawan-industrial-node">
    <img src="https://github-readme-stats.vercel.app/api/pin/?username=dev-nicolasv&repo=esp32-lorawan-industrial-node&theme=github_dark&hide_border=true&border_radius=12" alt="ESP32 LoRaWAN Industrial Node" />
  </a>
  <a href="https://github.com/dev-nicolasv/esp32-robust-ota-architecture">
    <img src="https://github-readme-stats.vercel.app/api/pin/?username=dev-nicolasv&repo=esp32-robust-ota-architecture&theme=github_dark&hide_border=true&border_radius=12" alt="ESP32 Robust OTA Architecture" />
  </a>
</p>

### 📡 ESP32 LoRaWAN Industrial Node

Industrial-grade ESP32 LoRaWAN node template focused on:

- ESP32
- Seeed LoRa-E5 through UART AT commands
- ADS1115 analog acquisition
- 4–20 mA industrial sensor input
- Compact binary payload encoding
- Deep Sleep optimization

**Architecture:** wake → measure → encode → uplink → sleep.

---

### 🔄 ESP32 Robust OTA Architecture

Production-oriented OTA firmware architecture focused on:

- FreeRTOS task isolation
- PID control task separation
- HTTPS firmware download
- SHA-256 firmware validation
- Dual OTA partitions
- Watchdog-aware design
- Automatic rollback protection

**Architecture:** keep critical control logic deterministic while OTA runs safely in parallel.

---

## 🏭 Field Projects

| Project | Area | Focus |
|---|---|---|
| 🌊 [Colbún Hydroelectric Early Warning System](https://www.youtube.com/watch?v=atfTgxQO1dA) | Energy / Monitoring | Environmental monitoring and alert system |
| 🚨 [SAT / EWARS Viña del Mar](https://www.youtube.com/watch?v=G301dtDWlcg) | Urban Risk Prevention | Early warning system development |
| ☁️ [Cloud Seeding System — Mettech Seerain](https://youtu.be/6tkjbmUdPcM) | Atmospheric Systems | Control hardware and embedded integration |
| ⚙️ [Custom Hardware & PCB Development](https://youtu.be/EI487dh6bS8) | Hardware Engineering | Board design, assembly, and firmware integration |
| 🎵 [Musical Swing — Sergafel](https://youtu.be/dYeEN-3rE7M) | Interactive Hardware | Robust public-use hardware |

---

## 📊 GitHub Metrics

<p align="center">
  <img height="180" src="https://github-readme-stats.vercel.app/api/top-langs/?username=dev-nicolasv&layout=compact&theme=github_dark&hide_border=true&border_radius=12&langs_count=8" alt="Most Used Languages" />
</p>

---

## 🧭 Engineering Profile Snapshot

<table>
<tr>
<td width="25%" align="center">

### ⚙️ Firmware

ESP32  
STM32  
C / C++  
FreeRTOS  

</td>
<td width="25%" align="center">

### 📡 IoT

LoRaWAN  
MQTT  
RS485  
Modbus RTU  

</td>
<td width="25%" align="center">

### 🔌 Hardware

Altium  
KiCad  
PCB Design  
Bring-Up  

</td>
<td width="25%" align="center">

### 🛡️ Reliability

OTA  
Rollback  
Watchdogs  
Diagnostics  

</td>
</tr>
</table>

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

I conduct online workshops and teach robotics to kids and teenagers, translating complex low-level engineering concepts into accessible learning experiences.

📺 [Watch a snippet of my Online Workshops](https://youtu.be/h6abCMyFRaY)

---

## 🤝 Connect

<p align="center">
  <a href="https://www.linkedin.com/in/nicol%C3%A1s-v%C3%A1squez-y%C3%A1%C3%B1ez-9b8684151/">
    <img src="https://img.shields.io/badge/LinkedIn-Nicolás%20Vásquez-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" />
  </a>
  <a href="https://www.upwork.com/freelancers/~01cc5ecb54a0f95fcc?viewMode=1">
    <img src="https://img.shields.io/badge/Upwork-Embedded%20IoT%20Developer-15803d?style=for-the-badge&logo=upwork&logoColor=white" alt="Upwork" />
  </a>
  <a href="https://github.com/dev-nicolasv">
    <img src="https://img.shields.io/badge/GitHub-dev--nicolasv-0b0f19?style=for-the-badge&logo=github&logoColor=white" alt="GitHub" />
  </a>
</p>

---

## ⚡ Engineering Philosophy

Embedded systems fail in the details:

- bad power design
- noisy signals
- poor recovery logic
- weak OTA strategy
- unclear diagnostics
- fragile prototypes
- untested edge cases

My job is to design firmware and hardware integration that anticipates those problems before the product reaches the field.

**Build it. Validate it. Deploy it. Keep it running.**

<p align="center">
  <img src="./assets/footer-industrial.svg" alt="Embedded systems engineered for the real world" width="100%" />
</p>
````
