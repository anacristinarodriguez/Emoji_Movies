from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os
from app.routes.auth import router as auth_router
from app.routes.recommend import router as recommend_router
from app.database import engine
from app import models

load_dotenv(override=True)
app = FastAPI()


GROQ_API_KEY = os.getenv("GROQ_API_KEY")
OMDB_API_KEY = os.getenv("OMDB_API_KEY")
SECRET_KEY = os.getenv("SECRET_KEY")
# Create tables
models.Base.metadata.create_all(bind=engine)

# Buse: CORS config
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(auth_router, prefix="/auth")
app.include_router(recommend_router)

# Static files
app.mount("/static", StaticFiles(directory="app/static"), name="static")

@app.get("/")
def read_index():
    return FileResponse("app/static/index.html")

@app.get("/watch.html", response_class=FileResponse)
def serve_watch():
    return FileResponse("app/static/watch.html")
