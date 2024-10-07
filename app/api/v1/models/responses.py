from pydantic import BaseModel
from typing import Optional, Any, List

class QueryResponse(BaseModel):
    response: Optional[str]
    status: str
    error: Optional[str] = None

class DocumentResponse(BaseModel):
    status: str
    error: Optional[str] = None

class HealthResponse(BaseModel):
    status: str
    statusCode: str
