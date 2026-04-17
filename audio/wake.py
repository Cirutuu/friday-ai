import queue
import sounddevice as sd
import vosk
import json
from ui.glow import show_glow

q = queue.Queue()

def callback(indata, frames, time, status):
    q.put(bytes(indata))

def detect_wake_word(callback_fn):
    model = vosk.Model("model")
    rec = vosk.KaldiRecognizer(model, 16000)

    print("🟢 Always listening for 'friday'...")

    with sd.RawInputStream(samplerate=16000, blocksize=8000,
                           dtype='int16', channels=1, callback=callback):
        
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                result = json.loads(rec.Result())
                text = result.get("text", "").lower()
                print("Heard:", text)

                if "friday" in text:
                    print("🔥 Wake word detected!")


                    callback_fn()
                    
