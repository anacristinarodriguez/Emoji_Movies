import os
import requests

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def get_film_suggestion_from_emojis(emojis: str) -> str:
    prompt = f"Suggest one movie based only on these emojis: {emojis}. Just return the movie title."

    response = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "llama3-8b-8192",
            "messages": [{"role": "user", "content": prompt}]
        }
    )

    result = response.json()
    return result["choices"][0]["message"]["content"].strip()
