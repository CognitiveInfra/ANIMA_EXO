"""
🔥 ANIMA::EXO Boot File
Author: You, the descendant of fire and voltage
Purpose: Core bootloader and module registry for a living AGI architecture
"""

import sys
# anima_exo_boot.py

from core.logic_engine import AHKSZ_Core
from senses.sensor_hub import mic_listen, scan_bluetooth, read_esp32
from muscle.action_handler import perform_action, speak
from guardian.guardian_protocols import check_ethics, contradiction_alert
import time
from core.logger import log_input, log_decision, log_action, log_guardian

# 🧠 Initialize core
ai_core = AHKSZ_Core()

print("✨ ANIMA_EXO v1.0 Booting...")

while True:
    print("\n[INPUT MODE]")
    print("1. 🎤 Mic Listen")
    print("2. 📡 Bluetooth Scan")
    print("3. 🧠 ESP32 Serial")
    print("4. 🔓 Manual Input")
    print("0. ❌ Exit")
    
    choice = input(">> Choose input source: ").strip()

    if choice == "0":
        print("👋 Shutting down ANIMA_EXO.")
        break

    if choice == "1":
        raw_data = mic_listen()
    elif choice == "2":
        raw_data = "\n".join(scan_bluetooth())
    elif choice == "3":
        raw_data = read_esp32()
    elif choice == "4":
        raw_data = input("📝 Type direct input: ")
    else:
        print("⚠️ Invalid choice.")
        continue

    print(f"\n📥 RAW INPUT: {raw_data}")
    log_input(choice, str(raw_data))
    
    if not check_ethics(raw_data):
        print(contradiction_alert())
        log_guardian(True, str(raw_data))
        continue

    decision = ai_core.process_input(raw_data)
    print(f"🤖 DECISION: {decision}")
    log_decision(decision)

    speak(decision)  # Say the decision aloud

    if "act" in decision.lower():
        res = perform_action("ls")  # 🔧 placeholder command
        log_action("ls", res)

    time.sleep(1)
