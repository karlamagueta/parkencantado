import pytest
from app.db import conn
from app.admin import get_content

@pytest.mark.unit
def test_positive_get_content():
    db = conn()
    cursor = db.cursor()

    result = get_content("termos_e_condicoes", "Termos de Uso")


    assert result[0][1] == "e"

    cursor.close()
    db.close()
