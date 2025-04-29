from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from app.routes.auth import router as auth_router
from app.routes.recommend import router as recommend_router
from app.database import engine
from app import models

load_dotenv()
app = FastAPI()

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
app.include_router(recommend_router, prefix="/recommend")

# Static files
app.mount("/static", StaticFiles(directory="app/static"), name="static")

@app.get("/")
def read_index():
    return FileResponse("app/static/index.html")
