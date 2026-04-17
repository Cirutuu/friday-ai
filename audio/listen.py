import queue
import sounddevice as sd
import vosk
import json

q = queue.Queue()

def callback(indata, frames, time, status):
    q.put(bytes(indata))

def listen_command():
    model = vosk.Model("model")
    rec = vosk.KaldiRecognizer(model, 16000)

    with sd.RawInputStream(samplerate=16000, blocksize=8000,
                           dtype='int16', channels=1, callback=callback):
        print("Listening for command...")

        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                result = json.loads(rec.Result())
                text = result.get("text", "")
                if text:
                    print("You said:", text)
                    return text
