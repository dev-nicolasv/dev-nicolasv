<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/field-reliability-console-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="./assets/field-reliability-console-light.svg">
  <img src="./assets/field-reliability-console-light.svg" alt="NV Field Reliability Console: ruta de señal desde sensor hasta campo, con diagnóstico y rollback" width="100%">
</picture>

# Nicolás Vásquez Yáñez

**Desarrollador de Sistemas Embebidos e IoT Industrial**<br>
Viña del Mar, Chile · ESP32 · STM32 · FreeRTOS · LoRaWAN · RS485/Modbus · OTA + rollback

> **Firmware diseñado para todo lo que viene después de la demostración.**

Diseño sistemas embebidos que avanzan desde el bring-up de la placa hasta un despliegue confiable en campo, con control determinista, conectividad industrial, diagnóstico y rutas de recuperación consideradas desde el inicio.

[Explorar sistemas seleccionados](#sistemas-seleccionados) · [Cómo diseño la confiabilidad](#confiabilidad-en-la-práctica) · [LinkedIn](https://www.linkedin.com/in/nicol%C3%A1s-v%C3%A1squez-y%C3%A1%C3%B1ez-9b8684151/) · [Upwork](https://www.upwork.com/freelancers/~01cc5ecb54a0f95fcc?viewMode=1) · [Read in English](./README.md)

## Evidencia de campo

- **Firmware y hardware como un solo sistema:** desde prototipos iniciales e integración de PCB hasta validación, puesta en marcha y robustecimiento orientado a campo.
- **Trabajo embebido de extremo a extremo:** firmware de MCU, arquitectura RTOS, señales industriales, enlaces cableados e inalámbricos, bring-up y diagnóstico.
- **Diseño para restricciones reales:** señales ruidosas, energía limitada, conectividad intermitente, mantenimiento remoto y recuperación segura.

Mi trabajo tiene mayor valor donde el firmware se encuentra con la realidad física: sensores, electrónica de control, comunicaciones, consumo de energía y los detalles operacionales que determinan si un dispositivo sigue funcionando después del despliegue.

## Sistemas seleccionados

### Sistemas de alerta temprana SAT / EWARS

**Contexto:** conectividad, monitoreo en tiempo real y despliegue operacional en terreno para sistemas de alerta temprana.<br>
**Territorio de ingeniería:** adquisición embebida, hardware de control, telemetría, integración y puesta en marcha.<br>
**Evidencia pública:** [demostración de conectividad y monitoreo](https://www.youtube.com/watch?v=atfTgxQO1dA) y [despliegue operacional en Colbún](https://www.youtube.com/watch?v=G301dtDWlcg).

Estos proyectos representan el tipo de trabajo sistémico que más valoro: transformar señales ambientales en información confiable y alertas sobre las que se pueda actuar.

### Nodo industrial ESP32 LoRaWAN

**Problema:** adquirir una señal industrial de 4-20 mA y transmitir telemetría compacta desde un nodo remoto con consumo controlado.<br>
**Arquitectura:** ESP32 + ADS1115 + módem LoRa-E5 mediante UART, codificación binaria del payload y deep sleep.<br>
**Restricción:** equilibrar calidad de medición, tamaño del payload, actividad de radio y consumo energético.<br>
**Evidencia:** [código y documentación](https://github.com/dev-nicolasv/esp32-lorawan-industrial-node) · [release v1.0.0](https://github.com/dev-nicolasv/esp32-lorawan-industrial-node/releases/tag/release-pro-v1.0.0).

### Arquitectura robusta de OTA para ESP32

**Problema:** actualizar firmware sin permitir que el trabajo de red comprometa el comportamiento del control crítico.<br>
**Arquitectura:** tareas FreeRTOS aisladas, descarga HTTPS, validación SHA-256, particiones OTA duales, ejecución compatible con watchdog y protección mediante rollback.<br>
**Restricción:** mantener determinista la ruta de control mientras la actualización y recuperación se ejecutan de forma independiente.<br>
**Evidencia:** [arquitectura de referencia pública](https://github.com/dev-nicolasv/esp32-robust-ota-architecture). Su documentación de validación y definición de licencia siguen ampliándose antes de afirmar que está lista para producción o que es open source.

<details>
<summary><strong>Más trabajo público en terreno</strong></summary>

- [Sistema de siembra de nubes](https://youtu.be/6tkjbmUdPcM)
- [PCB Levix Lite](https://youtu.be/EI487dh6bS8)
- [Proyecto de columpio musical](https://youtu.be/dYeEN-3rE7M)

</details>

## Confiabilidad en la práctica

| Capa de ingeniería | Objetivo de diseño |
| --- | --- |
| **Arranque y actualización seguros** | Validación de firmware, particiones duales, flujos acotados de actualización, rollback y estados explícitos de fallo |
| **Runtime determinista** | Tareas aisladas, máquinas de estado, estrategia de watchdog, reintentos acotados y rutas predecibles de control |
| **Interfaces industriales** | 4-20 mA, 0-10 V, adquisición ADC, RS485, Modbus RTU, relés y entradas o salidas digitales |
| **Diagnóstico y recuperación** | Logs útiles, payloads de estado, clasificación de errores, recuperación remota y comportamiento mantenible en campo |

**Plataformas y tecnologías:** ESP32, STM32, C/C++, FreeRTOS, ESP-IDF, PlatformIO, LoRaWAN, MQTT, WiFi, BLE, UART, SPI, I2C, CAN, XBee/DigiMesh, Altium Designer y KiCad.

## Laboratorio público de ingeniería

- **[esp32-lorawan-industrial-node](https://github.com/dev-nicolasv/esp32-lorawan-industrial-node)** - referencia de telemetría industrial de bajo consumo construida alrededor de adquisición 4-20 mA y uplink LoRaWAN.
- **[esp32-robust-ota-architecture](https://github.com/dev-nicolasv/esp32-robust-ota-architecture)** - referencia pública para separar las responsabilidades de control crítico, descarga, validación y recuperación; su licencia sigue pendiente.

Las descripciones de proyectos de este perfil son intencionalmente estáticas y legibles. La información importante no depende de tarjetas estadísticas, contadores o servicios externos de imágenes.

## Ahora y más allá de la ingeniería

Me interesan especialmente el monitoreo industrial, los sistemas de alerta temprana, la telemetría remota, OTA con rollback, gateways RS485/Modbus, nodos con batería o energía solar y productos que necesitan pasar de un prototipo inestable a un despliegue mantenible.

<details>
<summary><strong>Mentoría, talleres y el lado humano</strong></summary>

Me importa enseñar robótica y hacer que la ingeniería de bajo nivel sea más accesible. [Ver un extracto público de un taller](https://youtu.be/h6abCMyFRaY).

La fe también forma parte de cómo entiendo la responsabilidad, el servicio y el trabajo a largo plazo. Confío en Dios y procuro que esa convicción se refleje más en la constancia que en los eslóganes.

</details>

## Contacto

Estoy disponible para colaboraciones en sistemas embebidos e IoT industrial donde un prototipo necesite mejor arquitectura, integración con hardware, diagnóstico o un camino creíble hacia el despliegue en campo.

- [Conectar por LinkedIn](https://www.linkedin.com/in/nicol%C3%A1s-v%C3%A1squez-y%C3%A1%C3%B1ez-9b8684151/)
- [Conversar sobre un proyecto en Upwork](https://www.upwork.com/freelancers/~01cc5ecb54a0f95fcc?viewMode=1)
- [Explorar mi trabajo en GitHub](https://github.com/dev-nicolasv)

**Constrúyelo. Valídalo. Despliégalo. Mantenlo funcionando.**
