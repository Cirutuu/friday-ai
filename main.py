from audio.wake import detect_wake_word
from audio.listen import listen_command
from audio.speak import speak
from core.actions import execute
from audio.interrupt import listen_for_interrupt

import threading
import time

ACTIVE_TIMEOUT = 10


def run_jarvis():
    speak("Yes sir")

    last_active = time.time()

    while True:
        command = listen_command()

        if not command:
            continue

        print("👉 Command:", command)

        last_active = time.time()

        # 🛑 exit
        if "stop" in command or "sleep" in command:
            speak("Going silent")
            break

        # ⚡ process command
        response = execute(command)

        print("🤖 Response:", response)

        speak(response)

        # 💤 timeout
        if time.time() - last_active > ACTIVE_TIMEOUT:
            speak("Going to sleep")
            break

if __name__ == "__main__":
    detect_wake_word(run_jarvis)
