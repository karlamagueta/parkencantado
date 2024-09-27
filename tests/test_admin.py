import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.db import conn
from app.admin import get_all_content


@pytest.mark.unit
def test_positive_get_all_content():
    db = conn()
    cursor = db.cursor()

    result = get_all_content()


    assert result[0]['identifier'] == "termos"

    cursor.close()
    db.close()


@pytest.mark.unit
def test_positive_update_content():
    db = conn()
    cursor = db.cursor()
    client = TestClient(app)

    response = client.post(
        "/admin/update",
        data={
            "termos": "Novos termos de uso.",
            "sobre": "Nova descrição sobre o parque."
        }
    )

    assert response.status_code == 200
