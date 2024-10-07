
from fastapi import APIRouter
from app.api.v1.models.responses import HealthResponse

router = APIRouter()

@router.get("/")
def health_check():
    return HealthResponse(status="Success", statusCode="200 OK")