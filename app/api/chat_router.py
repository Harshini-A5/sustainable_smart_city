from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.granite_llm import ask_granite

router = APIRouter()

class Prompt(BaseModel):
    text: str

@router.post("/chat/ask")
async def chat_with_bot(prompt: Prompt):
    try:
        response = ask_granite(prompt.text)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
