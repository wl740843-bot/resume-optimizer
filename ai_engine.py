import requests
from config import API_KEY, BASE_URL, MODEL

def ask_ai(prompt, system_prompt="你是专业 HR"):
    url = f"{BASE_URL}/chat/completions"
    headers = {"Authorization": f"Bearer {API_KEY}"}
    data = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ]
    }
    resp = requests.post(url, headers=headers, json=data)
    return resp.json()["choices"][0]["message"]["content"]