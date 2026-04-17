import pyttsx3
import threading

engine = pyttsx3.init()
stop_signal = False

def speak(text):
    global stop_signal
    stop_signal = False

    def run():
        engine.say(text)
        engine.runAndWait()

    thread = threading.Thread(target=run)
    thread.start()

    return thread


def stop_speaking():
    global stop_signal
    stop_signal = True
    engine.stop()
