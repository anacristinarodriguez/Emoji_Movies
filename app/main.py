from dotenv import load_dotenv
from fastapi import FastAPI
from app.routes.auth import router as auth_router
from app.routes.recommend import router as recommend_router
from fastapi.staticfiles import StaticFiles





load_dotenv()
app = FastAPI()
app.mount("/", StaticFiles(directory="app/static", html=True), name="static")
app.include_router(auth_router, prefix="/auth")
app.include_router(recommend_router, prefix="/recommend")

@app.get("/")
def root():
    return {"message": "Movie Recommender API is up!"}
