from app.config import settings
from app.api.v1.router import api_router

from fastapi import FastAPI
from adalflow.components.model_client import GroqAPIClient
import time

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

app.include_router(api_router, prefix=settings.API_V1_STR)


