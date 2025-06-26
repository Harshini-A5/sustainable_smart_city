from fastapi import APIRouter, UploadFile, File
from app.services.granite_llm import generate_summary

router = APIRouter()

@router.post("/policy/summarize")
async def summarize_policy(file: UploadFile = File(...)):
    contents = await file.read()
    text = contents.decode("utf-8")
    summary = generate_summary(text)
    return {"summary": summary}
