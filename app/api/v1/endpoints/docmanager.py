
from fastapi import APIRouter, Depends, File, HTTPException, UploadFile

from app.api.v1.models.responses import DocumentResponse
from app.services.document_service import DocumentService, get_document_service


router = APIRouter()

@router.post("/upload")
async def upload_document(
    file: UploadFile,
    document_service: DocumentService = Depends(get_document_service)
):
    try:
        content = await file.read()
        document_service.process_document(content)
        return DocumentResponse(
            status="success"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))