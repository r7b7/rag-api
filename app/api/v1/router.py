
from fastapi import APIRouter

from app.api.v1.endpoints import docmanager, rag, healthcheck

api_router = APIRouter()

api_router.include_router(
    rag.router,
    prefix="/rag",
    tags=["RAG Operations"]
)

api_router.include_router(
    docmanager.router,
    prefix="/documents",
    tags=["Document Management"]
)

api_router.include_router(
    healthcheck.router,
    prefix="/health",
    tags=["Health Checks"]
)
