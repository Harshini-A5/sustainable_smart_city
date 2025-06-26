from fastapi import APIRouter

router = APIRouter()

@router.get("/eco-tip")
def get_tip():
    return {"tip": "Turn off lights when not in use."}
