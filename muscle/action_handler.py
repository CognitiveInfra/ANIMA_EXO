import subprocess

# ⚔️ Output / Action Module

def perform_action(command):
    print(f"⚔️ EXECUTING: {command}")
    result = subprocess.getoutput(command)
    return result

def speak(text):
    try:
        subprocess.run(["espeak", text])
    except Exception as e:
        print("espeak not available:", e)

def trigger_esp32_gpio(port='/dev/ttyUSB0', pin=2, state=1, baud=115200, duration=0.5):
    """Send a simple GPIO toggle command over serial to an attached ESP32.

    Notes:
    - This helper expects an ESP32 sketch that reads lines like: 'GPIO <pin> <state>\n'
    - If no serial device is present the function returns an error message.
    """
    try:
        import serial
    except Exception as e:
        return f"pyserial not installed: {e}"

    cmd = f"GPIO {pin} {int(bool(state))}\n"
    try:
        with serial.Serial(port, baud, timeout=1) as ser:
            ser.write(cmd.encode())
            time_sleep = duration
            # optional hold
            if time_sleep:
                import time
                time.sleep(time_sleep)
            # send off command if state was 1
            if state:
                ser.write(f"GPIO {pin} 0\n".encode())
            return "OK"
    except Exception as e:
        return f"Error talking to ESP32: {e}"
