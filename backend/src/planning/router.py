from fastapi import APIRouter
router = APIRouter()

@router.post("/")
async def create_plan(days: int = 5):
    return {"plan_id": 1, "days": days}
