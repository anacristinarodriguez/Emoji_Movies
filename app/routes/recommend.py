import requests
from fastapi import APIRouter, Depends, HTTPException, Header
from sqlalchemy.orm import Session
from jose import jwt, JWTError
from app.database import SessionLocal
from app.models import User, Preference
from app.utils import SECRET_KEY, ALGORITHM
from app.schemas.recommend import EmojiInput
from fastapi.security import OAuth2PasswordBearer


router = APIRouter()

GROQ_API_KEY = "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"
IMDB_API_KEY = "your_imdb_api_key"

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_current_user(
    authorization: str = Header(None), 
    db: Session = Depends(get_db)
):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Missing or invalid token")
    
    token = authorization.split(" ")[1]
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user = db.query(User).filter(User.username == payload.get("sub")).first()
        if user is None:
            raise HTTPException(status_code=401, detail="User not found")
        return user
    except JWTError:
        raise HTTPException(status_code=401, detail="Token invalid")

@router.post("/recommend/")
def recommend_movie(data: EmojiInput, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    llama_prompt = f"Suggest one film based on these emojis: {data.emojis}. Just return the film name."
    
    groq_response = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "llama3-8b-8192",
            "messages": [{"role": "user", "content": llama_prompt}]
        }
    )
    
    if groq_response.status_code != 200:
        raise HTTPException(status_code=500, detail="Groq API error")
    
    film_title = groq_response.json()["choices"][0]["message"]["content"].strip()

    # MOCKING IMDB RESPONSE
    top_film = {
        "title": film_title,
        "description": "A fantastic movie based on your selected emojis!",
        "image": "https://via.placeholder.com/150"
    }

    new_pref = Preference(emojis=data.emojis, movie_title=top_film["title"], user_id=user.id)
    db.add(new_pref)
    db.commit()

    return {
        "title": top_film["title"],
        "description": top_film["description"],
        "image": top_film["image"],
    }
