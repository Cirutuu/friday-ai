# Friday AI 🤖

> A fully offline, voice-controlled AI assistant inspired by Iron Man's JARVIS/FRIDAY — built for low-resource systems.

---

## ⚡ Features

* 🎤 Wake word detection ("Friday")
* 🧠 Local LLM (Ollama + TinyLlama)
* 🔄 Continuous conversation mode
* 🛑 Real-time interruption support
* ⚡ Fast command execution (no AI delay)
* 💾 Persistent memory system
* 🔒 Fully offline (no API required)

---

## 🧠 Architecture

```
Mic Input
   ↓
Speech Recognition (Vosk)
   ↓
Local LLM (Ollama) 🧠
   ↓
Text-to-Speech Output
```

---

## 🛠️ Tech Stack

* Python
* Vosk (speech recognition)
* Ollama (local LLM)
* TinyLlama (lightweight model)
* pyttsx3 (text-to-speech)

---

## ⚙️ Setup

```bash
# clone repo
git clone https://github.com/Cirutuu/friday-ai.git
cd friday-ai

# install dependencies
pip install -r requirements.txt

# install ollama
curl -fsSL https://ollama.com/install.sh | sh

# pull model
ollama pull tinyllama

# run
python main.py
```

---

## 🧪 Usage

Say:

```
friday
```

Then interact naturally:

```
what time is it
hello
```

---

## ⚠️ Notes

* Designed for low-RAM systems (~2GB usable)
* Uses hybrid execution (fast commands + LLM fallback)
* Speech recognition may require tuning for different accents
* Ran on Lubuntu OS

---

## 🚀 Future Improvements

* Smarter memory (auto-learning)
* GUI / HUD interface
* Multi-device sync
* Remote control (phone → laptop)

---

## ⭐ If you like this project

Give it a star — it helps a lot.
