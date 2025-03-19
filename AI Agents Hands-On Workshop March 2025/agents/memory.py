class MemoryAgent:
    def __init__(self):
        self.rules = {
            "hello": "Hi there!",
            "how are you": "I'm good, thank you!",
            "bye": "Goodbye!",
            "default": "I'm sorry, I don't understand"
        }
        self.memory = []

    def respond(self, user_input):
        self.memory.append(f"You: {user_input}")
        user_input = user_input.lower().strip()

        if user_input.startswith("my name is "):
            name = user_input[11:]
            self.memory.append(f"Agent: Got it, your name is {name}!")
            return f"Got it, your name is {name}!"
        elif user_input == "what's my name?" and any("your name is" in m for m in self.memory):
            for m in reversed(self.memory):
                if "your name is" in m:
                    name = m.split("your name is ")[1].strip("!")
                    return f"I remmeber, your name is {name}!"
        return self.rules.get(user_input, "I dont get it!")