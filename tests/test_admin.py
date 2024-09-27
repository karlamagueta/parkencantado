import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.db import conn
from app.admin import get_all_content, get_content


@pytest.mark.unit
def test_positive_get_content():
    db = conn()
    cursor = db.cursor()

    result = get_content("regulamento")
    assert result['identifier'] == "regulamento"

    cursor.close()
    db.close()


@pytest.mark.unit
def test_positive_get_all_content():
    db = conn()
    cursor = db.cursor()

    result = get_all_content()
    assert "regulamento" in result

    cursor.close()
    db.close()


@pytest.mark.unit
def test_positive_update_content():
    client = TestClient(app)

    text = "Nova descrição sobre o parque."
    response = client.post(
        "/admin/regulamento",
        data={
            "content": text
        }
    )

    assert response.status_code == 200

    assert get_content("regulamento")["content"] == text
