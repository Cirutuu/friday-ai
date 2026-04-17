import requests

def ask_ai(command):
    try:
        response = requests.post(
            "http://127.0.0.1:11434/api/generate",
            json={
                "model": "tinyllama",
                "prompt": f"{command}. Giive short and direct ans\nFriday:",
                "stream": False
            },
            timeout=120
        )

        data = response.json()
        return data.get("response", "").strip()

    except Exception as e:
        print("ERROR:", e)
        return "Local AI not responding"
