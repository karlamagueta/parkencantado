from .db import session_conn
from uuid import uuid4

def set_session(username):
    session_id = uuid4().hex
    db = session_conn()
    cursor = db.cursor()

    cursor.execute(
        "INSERT INTO session (session_id, username) VALUES (?, ?)",
        (session_id, username)
    )

    db.commit()
    db.close()

    return session_id


def get_session(session_id):
    db = session_conn()
    cursor = db.cursor()

    cursor.execute("SELECT username FROM session WHERE session_id = ?", (session_id,))
    row = cursor.fetchone()
    db.close()

    if row: # ("foo",)
        return row[0]


def delete_session(session_id):
    db = session_conn()
    cursor = db.cursor()

    cursor.execute("DELETE FROM session WHERE session_id = ?", (session_id,))

    db.commit()
    db.close()
