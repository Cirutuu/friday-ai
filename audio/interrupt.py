from audio.listen import listen_command
from audio.speak import stop_speaking

def listen_for_interrupt():
    while True:
        command = listen_command()

        if command and "stop" in command:
            print("🛑 Interrupt detected!")
            stop_speaking()
            break
