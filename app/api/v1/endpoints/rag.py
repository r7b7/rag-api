from fastapi import APIRouter, Depends, HTTPException

from app.api.v1.models.requests import QueryRequest
from app.api.v1.models.responses import QueryResponse
from app.services.rag_service import RAGService, get_rag_service

router = APIRouter()

@router.post("/query")
async def process_query(
    query: QueryRequest,
    rag_service: RAGService = Depends(get_rag_service)
):
    try:
        response = await rag_service.process_query(query.text)
        return QueryResponse(
            response=response,
            status="success"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))