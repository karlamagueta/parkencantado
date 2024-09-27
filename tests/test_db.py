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
    query = cursor.execute("SELECT * FROM content")
    assert query is not None
    db.close()
