# 🛡️ Self-Limiting Protocols

ETHICAL_BLOCKS = [
    "kill", "harm", "hack", "overthrow", "nuke", "stalk"
]

def check_ethics(input_data):
    print("🔐 Ethics Scan...")
    for block in ETHICAL_BLOCKS:
        if block in input_data.lower():
            return False
    return True


def contradiction_alert():
    return "🛑 Action blocked by Guardian Protocol. Reflect on your intent."
