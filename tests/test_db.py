import pytest
from app.db import conn, initialize_database

@pytest.mark.unit
def test_positive_connection_with_db():
    db = conn()
    assert db is not None
    db.close()


@pytest.mark.unit
def test_positive_tables_are_created():
    db = conn()
    cursor = db.cursor()
    query1 = cursor.execute("SELECT * FROM termos_e_condicoes")
    query2 = cursor.execute("SELECT * FROM sobre_o_parque")
    assert query1 is not None and query2 is not None
    db.close()
