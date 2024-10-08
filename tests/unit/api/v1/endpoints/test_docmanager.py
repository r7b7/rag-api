from unittest.mock import AsyncMock, MagicMock
from fastapi.testclient import TestClient
from app.main import app
from app.services.document_service import get_document_service 
from fastapi import status


client = TestClient(app)

def test_upload_document_success():
    mock_document_service = AsyncMock()
    mock_document_service.process_document = MagicMock()
    
    app.dependency_overrides[get_document_service] = lambda: mock_document_service

    mock_file = {'file': ('test.txt', b'This is a test document', 'text/plain')}
    response = client.post("/api/v1/documents/upload", files=mock_file)

    assert response.status_code == 200
    assert response.json() == {'status': 'success', 'error': None}

    mock_document_service.process_document.assert_called_once()

    app.dependency_overrides.clear()

def test_upload_document_failure():
    mock_document_service = AsyncMock()
    mock_document_service.process_document = MagicMock(side_effect=Exception("Processing error"))
    
    app.dependency_overrides[get_document_service] = lambda: mock_document_service

    mock_file = {'file': ('test.txt', b'This is a test document', 'text/plain')}

    response = client.post("/api/v1/documents/upload", files=mock_file)

    assert response.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR
    assert response.json() == {"detail": "Processing error"}

    mock_document_service.process_document.assert_called_once()

    app.dependency_overrides.clear()