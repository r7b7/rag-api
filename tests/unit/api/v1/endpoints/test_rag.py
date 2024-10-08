from unittest.mock import AsyncMock, MagicMock
from fastapi.testclient import TestClient
from app.api.v1.models.requests import QueryRequest
from app.main import app
from app.services.rag_service import get_rag_service 

client = TestClient(app)

def test_upload_document_success():
    mock_rag_service = AsyncMock()
    mock_rag_service.process_query.return_value = "test response"
    
    app.dependency_overrides[get_rag_service] = lambda: mock_rag_service

    request_payload = {"text": "Sample query"}    
    response = client.post("/api/v1/rag/query", json=request_payload)

    assert response.status_code == 200
    assert response.json() == {"response":"test response","status": "success","error":None}
    
    mock_rag_service.process_query.assert_called_once()

    app.dependency_overrides.clear()