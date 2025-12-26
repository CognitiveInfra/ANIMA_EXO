## System Dependencies (optional)
To enable audio, Bluetooth, and TTS features install the following system packages:

```bash
sudo apt update
sudo apt install -y libportaudio2 portaudio19-dev bluez espeak
```

Then install Python dependencies:

```bash
python3 -m pip install --user -r requirements.txt
```

Notes:
- `libportaudio2` and `portaudio19-dev` provide PortAudio for `sounddevice`.
- `bluez` enables Bluetooth scanning tools on Linux.
- `espeak` provides simple TTS via the `speak()` helper.
# ANIMA_EXO
