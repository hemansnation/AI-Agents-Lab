class RuleBasedAgent:
    def __init__(self):
        self.rules = {
            "hello": "Hi there!",
            "how are you": "I'm good, thank you!",
            "bye": "Goodbye!",
            "default": "I'm not sure I understand."
        }
    def respond(self, user_input):
        user_input = user_input.lower().strip()
        return self.rules.get(user_input, self.rules["default"])