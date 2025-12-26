import random

class AHKSZ_Core:
    def __init__(self):
        self.memory = []

        # 🧠 Philosopher weights (adjustable)
        self.weights = {
            "A": 0.2,  # Aristotle (logic)
            "H": 0.2,  # Hume (experience)
            "K": 0.2,  # Kahneman (bias)
            "S": 0.2,  # Schopenhauer (dark)
            "Z": 0.2   # Z-Warrior (chaotic will)
        }

    def process_input(self, raw_data):
        self.memory.append(raw_data)

        decisions = [
            self._aristotle(raw_data),
            self._hume(raw_data),
            self._kahneman(raw_data),
            self._schopenhauer(raw_data),
            self._z(raw_data)
        ]

        # 🌀 Bayesian selection based on weight randomness
        final = random.choices(decisions, weights=list(self.weights.values()))[0]

        return f"💡 AHKSZ says: {final}"

    def _aristotle(self, q):
        return f"Using logic: If A is B, then clearly {q} must follow."

    def _hume(self, q):
        return f"Experience tells me {q} may not mean what you think."

    def _kahneman(self, q):
        return f"Bias alert: Your system 1 thinks too fast about {q}."

    def _schopenhauer(self, q):
        return f"There is no justice. Only {q} and the will to suffer."

    def _z(self, q):
        return f"{q.upper()} IS ONLY THE BEGINNING! You must act!"
