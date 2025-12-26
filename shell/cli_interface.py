# 🧬 CLI interface for communicating with EXO
def launch_cli(ai_core):
    print("💻 ANIMA::EXO Terminal Ready.")
    while True:
        user_input = input("EXO> ")
        if user_input.lower() in ["exit", "quit"]:
            print("🛑 Shutting down.")
            break
        response = ai_core.process_input(user_input)
        print(f"→ {response}")
