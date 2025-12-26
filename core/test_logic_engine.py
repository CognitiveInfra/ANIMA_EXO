from core.logic_engine import AHKSZ_Core

def main():
    core = AHKSZ_Core()
    tests = [
        "hello world",
        "should we act now?",
        "dangerous plan"
    ]

    for t in tests:
        print("INPUT:", t)
        print(core.process_input(t))
        print("---")

if __name__ == '__main__':
    main()
