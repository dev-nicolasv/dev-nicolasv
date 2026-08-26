<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/field-reliability-console-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="./assets/field-reliability-console-light.svg">
  <img src="./assets/field-reliability-console-light.svg" alt="NV Field Reliability Console mostrando una ruta operacional desde el sensor hasta el campo" width="100%">
</picture>

# Nicolás Vásquez Yáñez

**Desarrollador de Sistemas Embebidos e IoT Industrial**<br>
Viña del Mar, Chile · Firmware, electrónica, conectividad y confiabilidad en campo

> **Firmware diseñado para todo lo que viene después de la demostración.**

Diseño sistemas embebidos que avanzan desde el bring-up de la placa hasta un despliegue confiable en campo. Mi trabajo conecta control determinista, señales industriales, telemetría remota, diagnóstico y recuperación en un sistema mantenible.

[Sistemas seleccionados](#sistemas-seleccionados) · [Matriz de confiabilidad](#matriz-de-confiabilidad) · [Field Ops Live](#field-ops-live) · [Contacto](#contacto) · [Read in English](./README.md)

## Estado operacional

<p align="center">
  <a href="https://github.com/dev-nicolasv/esp32-lorawan-industrial-node/actions/workflows/platformio.yml"><img alt="Estado del CI PlatformIO del nodo LoRaWAN" src="https://github.com/dev-nicolasv/esp32-lorawan-industrial-node/actions/workflows/platformio.yml/badge.svg?branch=main"></a>
  <a href="https://github.com/dev-nicolasv/esp32-robust-ota-architecture/actions/workflows/firmware-ci.yml"><img alt="Estado del CI de firmware de la arquitectura OTA" src="https://github.com/dev-nicolasv/esp32-robust-ota-architecture/actions/workflows/firmware-ci.yml/badge.svg?branch=main"></a>
  <a href="https://github.com/dev-nicolasv/dev-nicolasv/actions/workflows/update-engineering-status.yml"><img alt="Sincronización del estado Field Ops" src="https://github.com/dev-nicolasv/dev-nicolasv/actions/workflows/update-engineering-status.yml/badge.svg?branch=main"></a>
  <a href="https://github.com/dev-nicolasv/esp32-lorawan-industrial-node/releases/latest"><img alt="Última release del nodo LoRaWAN" src="https://img.shields.io/github/v/release/dev-nicolasv/esp32-lorawan-industrial-node?display_name=tag&style=flat-square&label=LoRaWAN%20release&color=0ea5e9"></a>
  <a href="https://github.com/dev-nicolasv/esp32-lorawan-industrial-node/blob/main/LICENSE"><img alt="Licencia del repositorio LoRaWAN" src="https://img.shields.io/github/license/dev-nicolasv/esp32-lorawan-industrial-node?style=flat-square&label=LoRaWAN%20license&color=22c55e"></a>
</p>

`FIELD / ACTIVE` Desde prototipos iniciales e integración de PCB hasta validación, puesta en marcha y robustecimiento orientado a campo. Me concentro en las restricciones que deciden si un dispositivo sigue funcionando después del despliegue: señales ruidosas, energía limitada, conectividad intermitente, mantenimiento remoto y recuperación controlada.

## Sistemas seleccionados

### SAT / EWARS · Sistemas de alerta temprana en terreno

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/sat-ewars-field-card-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="./assets/sat-ewars-field-card-light.svg">
  <img src="./assets/sat-ewars-field-card-light.svg" alt="Ruta de un sistema SAT y EWARS desde la medición ambiental hasta telemetría, monitoreo y respuesta operacional" width="100%">
</picture>

**Contexto:** conectividad, monitoreo en tiempo real y despliegue operacional en terreno para sistemas de alerta temprana.<br>
**Territorio de ingeniería:** adquisición embebida, hardware de control, telemetría, integración y puesta en marcha.<br>
**Evidencia pública:** [demostración de conectividad y monitoreo](https://www.youtube.com/watch?v=atfTgxQO1dA) · [despliegue operacional en Colbún](https://www.youtube.com/watch?v=G301dtDWlcg)

Estos sistemas representan el trabajo que más valoro: transformar señales ambientales en información confiable y alertas sobre las que se pueda actuar.

<table>
  <tr>
    <td width="50%" valign="top">
      <picture>
        <source media="(prefers-color-scheme: dark)" srcset="./assets/lorawan-node-card-dark.svg">
        <source media="(prefers-color-scheme: light)" srcset="./assets/lorawan-node-card-light.svg">
        <img src="./assets/lorawan-node-card-light.svg" alt="Arquitectura de un nodo ESP32 LoRaWAN desde la adquisición 4-20 mA hasta el uplink de radio de bajo consumo" width="100%">
      </picture>
      <h3>Nodo industrial ESP32 LoRaWAN</h3>
      <p><strong>Problema:</strong> adquirir una señal industrial de 4-20 mA y enviar telemetría compacta desde un nodo remoto con consumo controlado.</p>
      <p><strong>Diseño:</strong> ESP32 + ADS1115 + LoRa-E5 mediante UART, codificación binaria del payload y luego deep sleep.</p>
      <p><strong>Evidencia:</strong> <a href="https://github.com/dev-nicolasv/esp32-lorawan-industrial-node">código y documentación</a> · <a href="https://github.com/dev-nicolasv/esp32-lorawan-industrial-node/releases/tag/release-pro-v1.0.0">release v1.0.0</a> · licencia MIT.</p>
    </td>
    <td width="50%" valign="top">
      <picture>
        <source media="(prefers-color-scheme: dark)" srcset="./assets/robust-ota-card-dark.svg">
        <source media="(prefers-color-scheme: light)" srcset="./assets/robust-ota-card-light.svg">
        <img src="./assets/robust-ota-card-light.svg" alt="Arquitectura de referencia OTA para ESP32 que separa control determinista, descarga, validación y rollback" width="100%">
      </picture>
      <h3>Arquitectura robusta de OTA para ESP32</h3>
      <p><strong>Problema:</strong> actualizar firmware sin permitir que el trabajo de red comprometa el comportamiento del control crítico.</p>
      <p><strong>Diseño:</strong> tareas FreeRTOS aisladas, descarga HTTPS, validación SHA-256, particiones OTA duales, ejecución compatible con watchdog y protección mediante rollback.</p>
      <p><strong>Estado:</strong> <a href="https://github.com/dev-nicolasv/esp32-robust-ota-architecture">arquitectura de referencia pública</a> · licencia pendiente.</p>
    </td>
  </tr>
</table>

## Tecnología por capas

<p>
  <img alt="Tag de firmware ESP32" src="https://img.shields.io/badge/MCU-ESP32-0ea5e9?style=flat-square&logo=espressif&logoColor=white">
  <img alt="Tag de firmware STM32" src="https://img.shields.io/badge/MCU-STM32-0ea5e9?style=flat-square&logo=stmicroelectronics&logoColor=white">
  <img alt="Tag de C y C++" src="https://img.shields.io/badge/LANG-C%2FC%2B%2B-334155?style=flat-square">
  <img alt="Tag de FreeRTOS" src="https://img.shields.io/badge/RTOS-FreeRTOS-0ea5e9?style=flat-square">
  <img alt="Tag de LoRaWAN" src="https://img.shields.io/badge/LPWAN-LoRaWAN-2563eb?style=flat-square">
  <img alt="Tag de RS485 y Modbus" src="https://img.shields.io/badge/FIELD-RS485%20%2F%20Modbus-2563eb?style=flat-square">
  <img alt="Tag de OTA y rollback" src="https://img.shields.io/badge/UPDATE-OTA%20%2B%20rollback-f59e0b?style=flat-square">
  <img alt="Tag de IoT industrial" src="https://img.shields.io/badge/DOMAIN-Industrial%20IoT-475569?style=flat-square">
</p>

| Capa | Herramientas de ingeniería | Qué permite construir |
| --- | --- | --- |
| **MCU y runtime** | ESP32, STM32, C/C++, FreeRTOS, ESP-IDF, PlatformIO | Tareas deterministas, máquinas de estado y ejecución compatible con watchdog |
| **Señales y E/S** | 4-20 mA, 0-10 V, ADC, relés, E/S digital | Adquisición y control confiables en la frontera física |
| **Conectividad** | LoRaWAN, MQTT, WiFi, BLE, RS485, Modbus RTU, CAN, XBee/DigiMesh | Telemetría y comandos mediante enlaces locales y remotos |
| **Integración de placa** | UART, SPI, I2C, Altium Designer, KiCad | Bring-up, integración de periféricos y firmware consciente del hardware |

## Matriz de confiabilidad

| Riesgo operacional | Respuesta de diseño | Objetivo operacional |
| --- | --- | --- |
| **Arranque o actualización inválidos** | Validación de firmware, particiones duales, flujos acotados y estados explícitos de fallo | Permitir recuperación y rollback controlado |
| **Interferencia en runtime** | Aislamiento de tareas, máquinas de estado, estrategia de watchdog y reintentos acotados | Preservar rutas predecibles de control bajo carga |
| **Interfaces ruidosas o imperfectas** | Consideración del acondicionamiento, validación, timeouts y clasificación de errores | Mantener mediciones útiles y degradar de forma controlada |
| **Diagnóstico remoto** | Estados estructurados, logs útiles, señales de salud y rutas de recuperación | Acortar el diagnóstico y reducir la intervención en terreno |

## Field Ops Live

El panel siguiente resume señales públicas de ingeniería de mis repositorios. Se genera dentro de este repositorio de perfil y complementa los badges oficiales de workflows mostrados arriba.

[![Panel Field Ops Live con estado de CI, releases y sincronización de repositorios](https://raw.githubusercontent.com/dev-nicolasv/dev-nicolasv/output/engineering-status.svg)](https://github.com/dev-nicolasv/dev-nicolasv/actions)

**Fallback accesible:** [workflow de LoRaWAN](https://github.com/dev-nicolasv/esp32-lorawan-industrial-node/actions/workflows/platformio.yml) · [workflow de firmware OTA](https://github.com/dev-nicolasv/esp32-robust-ota-architecture/actions/workflows/firmware-ci.yml) · [releases de LoRaWAN](https://github.com/dev-nicolasv/esp32-lorawan-industrial-node/releases/latest) · OTA: arquitectura de referencia pública, licencia pendiente.

## Misión actual

```text
$ focus --now
> telemetría remota confiable | runtimes embebidos deterministas

$ engineer --for
> enlaces intermitentes | energía limitada | actualizaciones recuperables

$ collaboration --status
> disponible para proyectos seleccionados de sistemas embebidos e IoT industrial
```

Me interesan especialmente el monitoreo industrial, los sistemas de alerta temprana, OTA recuperable, gateways RS485/Modbus, nodos con batería o energía solar y productos que avanzan desde un prototipo inestable hasta un despliegue mantenible.

<details>
<summary><strong>Experiencia en campo, mentoría y el lado humano</strong></summary>

### Más trabajo público en terreno

- [Sistema de siembra de nubes](https://youtu.be/6tkjbmUdPcM)
- [PCB Levix Lite](https://youtu.be/EI487dh6bS8)
- [Proyecto de columpio musical](https://youtu.be/dYeEN-3rE7M)

### Mentoría y talleres

Me importa enseñar robótica y hacer que la ingeniería de bajo nivel sea más accesible. [Ver un extracto público de un taller](https://youtu.be/h6abCMyFRaY).

La fe también forma parte de cómo entiendo la responsabilidad, el servicio y el trabajo a largo plazo. Confío en Dios y procuro que esa convicción se refleje más en la constancia que en los eslóganes.

</details>

## Contacto

Estoy disponible para colaboraciones en sistemas embebidos e IoT industrial donde un prototipo necesite mejor arquitectura, integración con hardware, diagnóstico o un camino creíble hacia el despliegue en campo.

<p>
  <a href="https://www.linkedin.com/in/nicol%C3%A1s-v%C3%A1squez-y%C3%A1%C3%B1ez-9b8684151/"><img alt="Conectar con Nicolás en LinkedIn" src="https://img.shields.io/badge/LinkedIn-conectar-0a66c2?style=flat-square&logo=linkedin&logoColor=white"></a>
  <a href="https://www.upwork.com/freelancers/~01cc5ecb54a0f95fcc?viewMode=1"><img alt="Conversar con Nicolás sobre un proyecto en Upwork" src="https://img.shields.io/badge/Upwork-conversar%20un%20proyecto-14a800?style=flat-square&logo=upwork&logoColor=white"></a>
</p>

[Explorar mi trabajo en GitHub](https://github.com/dev-nicolasv)

**Constrúyelo. Valídalo. Despliégalo. Mantenlo funcionando.**
