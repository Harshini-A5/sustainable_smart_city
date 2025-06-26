from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()
feedback_storage = []

class Feedback(BaseModel):
    name: str
    category: str
    message: str

@router.post("/submit-feedback")
async def submit_feedback(feedback: Feedback):
    feedback_storage.append(feedback.dict())
    return {"message": "Feedback submitted successfully"}
