ESP32 GPIO helper
=================

Files:
- `esp32_gpio.ino` — simple Arduino sketch that listens on serial for commands `GPIO <pin> <state>` (see `extras/esp32/esp32_gpio.ino`).
- `platformio.ini` — minimal PlatformIO configuration for `esp32dev`.

Build & Upload (PlatformIO)
---------------------------

1. Install PlatformIO (VSCode extension) or the PlatformIO CLI.
2. Open this folder in VSCode and select the PlatformIO project located in `extras/esp32`.
3. Build and Upload to your ESP32 with the IDE controls, or run from command line:

```bash
cd extras/esp32
platformio run --target upload -e esp32dev
```

Using Arduino IDE
-----------------
1. Open `esp32_gpio.ino` in Arduino IDE.
2. Choose board `ESP32 Dev Module` and correct COM port.
3. Upload.

Host usage
----------
From Python you can call `trigger_esp32_gpio(port, pin, state)` from `muscle/action_handler.py` which sends `GPIO <pin> <state>` over serial. Example:

```python
from muscle.action_handler import trigger_esp32_gpio
print(trigger_esp32_gpio('/dev/ttyUSB0', pin=2, state=1))
```

Notes
-----
- Ensure serial baud (115200) matches the sketch.
- The sketch replies with `OK GPIO <pin> <state>` on success.
