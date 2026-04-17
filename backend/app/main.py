from fastapi import FastAPI

from app.db.database import Base, engine
from app.db import models
from app.api.chat import router as chat_router
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

load_dotenv()



app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "https://ai-platform-mu-hazel.vercel.app",
        "*"
    ],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


Base.metadata.create_all(bind=engine)

app.include_router(chat_router)


@app.get("/")
def root():
    return {"message": "API running"}
