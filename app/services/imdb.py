import os
import requests

IMDB_API_KEY = os.getenv("IMDB_API_KEY")

def search_movie(title: str):
    response = requests.get(f"https://imdb-api.com/en/API/SearchMovie/{IMDB_API_KEY}/{title}")
    data = response.json()
    if not data.get("results"):
        return None
    return data["results"][0]  # Return top result
