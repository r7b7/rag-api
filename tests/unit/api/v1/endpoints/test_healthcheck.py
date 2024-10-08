from fastapi.testclient import TestClient
from app.main import app 

client = TestClient(app)

class TestHealthEndpoint:
    def test_health_check_returns_200(self):
        response = client.get("/api/v1/health/")
        assert response.status_code == 200

    def test_health_check_returns_correct_data(self):
        response = client.get("/api/v1/health/")
        data = response.json()
        
        assert data["status"] == "Success"
        assert data["statusCode"] == "200 OK"

    def test_health_check_response_structure(self):
        response = client.get("/api/v1/health/")
        data = response.json()
        
        assert isinstance(data, dict)
        assert "status" in data
        assert "statusCode" in data
        
    def test_health_check_headers(self):
        response = client.get("/api/v1/health/")
        assert response.headers["content-type"] == "application/json"
        
    