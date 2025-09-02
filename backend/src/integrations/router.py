from fastapi import APIRouter
router = APIRouter()

@router.get("/health")
async def integrations_health():
    return {"ok": True}
