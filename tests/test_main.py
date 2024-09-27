import pytest
from fastapi.testclient import TestClient
from app.main import app
from unittest.mock import patch

client = TestClient(app)

@pytest.mark.unit
def test_positive_home_route():
    response = client.get("/")
    assert response.status_code == 200

@pytest.mark.unit
def test_positive_admin_route():
    response = client.get("/admin")
    assert response.status_code == 200

@pytest.mark.unit
@patch("app.main.send")
def test_positive_send_email(mock_send):
    response = client.post("/enviar-email/", data={
        "nome": "Test User",
        "email": "test@example.com",
        "telemovel": "123456789",
        "data": "2023-09-23",
        "mensagem": "Test message"
    })
    assert response.status_code == 200
    assert mock_send.call_count == 2
