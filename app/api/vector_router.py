from fastapi import APIRouter

router = APIRouter()

@router.get("/vector")
def get_vector():
    return {"message": "Vector endpoint working!"}
