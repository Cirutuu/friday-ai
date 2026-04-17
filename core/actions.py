from core.memory import remember, recall
import os
from core.brain import ask_ai


def execute(command):
    command = command.lower()

    # 🧠 STORE MEMORY
    if "my name is" in command:
        name = command.split("my name is")[-1].strip()
        remember("name", name)
        return f"Got it, {name}"

    # 🧠 RECALL MEMORY
    elif "what is my name" in command or "who am i" in command:
        name = recall("name")
        if name:
            return f"Your name is {name}"
        else:
            return "I don't know your name yet"

    # ⚡ FAST COMMANDS
    elif "time" in command:
        from datetime import datetime
        return datetime.now().strftime("%H:%M")

    elif "chrome" in command:
        os.system("xdg-open https://google.com")
        return "Opening Chrome"

    elif "hello" in command:
        name = recall("name")
        if name:
            return f"Hello {name}"
        return "Hello"

    # 🧠 fallback
    return ask_ai(command)
