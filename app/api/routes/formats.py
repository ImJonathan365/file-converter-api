from fastapi import APIRouter
from app.config.settings import settings

router = APIRouter()

@router.get("/", tags=["formats"])
def get_supported_formats():
    return {"supported_conversions": settings.supported_conversions}
