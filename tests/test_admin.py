import pytest
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
