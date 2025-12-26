# WHAT ANIMA::EXO IS

ANIMA::EXO is a small, modular project skeleton for experimenting with an architecture that pairs simple philosophical reasoning, sensor inputs, action modules, and a guardian ethics layer. It is intentionally lightweight and designed for rapid prototyping rather than production-ready AI.

Purpose
- Provide an extendable playground for thinking about: reasoning pipelines, sensor integration (audio, Bluetooth, serial), action execution (commands, TTS, device toggles), and safety gating.
- Demonstrate wiring of modules, logging, tests, and CI so you can iterate quickly.

High-level Architecture
- `core` — `AHKSZ_Core` reasoning engine (Aristotle, Hume, Kahneman, Schopenhauer, Z) with a simple decision selector.
- `senses` — sensor interfaces: `mic_listen`, `scan_bluetooth`, `read_esp32` (serial). Plug in real drivers or mocks.
- `muscle` — action handlers: `perform_action`, `speak`, and `trigger_esp32_gpio` for device control.
- `guardian` — ethical checks and blocking rules to prevent dangerous commands.
- `shell` — CLI interface and the `anima_exo_boot.py` boot script (interactive loop).
- `core/logger.py` — structured JSON logging with rotation; `web/` contains a tiny Flask UI to view live logs.

How to run (local)
1. Install Python deps:
   ```bash
   python3 -m pip install --user -r requirements.txt
   ```
2. (Optional) Install system packages for audio/Bluetooth/TTS on Debian/Ubuntu:
   ```bash
   sudo apt update
   sudo apt install -y libportaudio2 portaudio19-dev bluez espeak
   ```
3. Run tests:
   ```bash
   python3 -m unittest tests.test_all -v
   ```
4. Start the interactive boot script:
   ```bash
   python3 anima_exo_boot.py
   ```
5. (Optional) Run the live log UI:
   ```bash
   python3 web/app.py
   # then open http://localhost:8080
   ```

ESP32 Support
- See `extras/esp32/esp32_gpio.ino` for a minimal Arduino sketch that accepts `GPIO <pin> <state>` over serial.
- PlatformIO config in `extras/esp32/platformio.ini` and instructions in `extras/esp32/README.md`.

Repository & CI
- The repository contains GitHub Actions workflows in `.github/workflows/` to run tests and produce coverage artifacts. Push to GitHub to trigger CI.

Security & Safety
- The `guardian` module contains a simple blacklist; review and harden before enabling any unrestricted action execution or network access.
- Avoid running actions that execute arbitrary shell commands in untrusted environments.

Next Steps (recommended)
- Harden the guardian rules and add explicit command whitelisting for `perform_action()`.
- Add integration tests and mocks for sensors and ESP32.
- Enhance logger (structured fields), rotate/upload logs, and tighten CI (coverage badges).
- Build a minimal web control UI (authenticated) if you want remote control.

License & Contributing
- This skeleton contains no license by default — add a `LICENSE` file if you want to open-source it. Contributions welcome; follow the repo's guidelines.
