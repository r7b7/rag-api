from pydantic import BaseModel, Field
from typing import Optional, List

class QueryRequest(BaseModel):
    text: str = Field(min_length=10, max_length=2000)
    

class DocumentRequest(BaseModel):
    content: str
    metadata: Optional[dict] = None