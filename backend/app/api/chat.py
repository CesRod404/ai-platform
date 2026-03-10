from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel

from app.db.database import get_db
from app.services.llm_service import ask_llm

router = APIRouter()


class ChatRequest(BaseModel):
    message: str


@router.post("/chat")
def chat(request: ChatRequest, db: Session = Depends(get_db)):

    response = ask_llm(db, request.message)

    return {
        "response": response
    }
