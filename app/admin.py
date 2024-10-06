from app.db import conn
from datetime import datetime

def get_content(title: str):
    db = conn()
    cursor = db.cursor()

    cursor.execute(
        "SELECT identifier, title, content FROM content WHERE identifier = ?",
        (title,)
    )
    row = cursor.fetchone()
    if row:
        return dict(zip(["identifier", "title", "content"], row))


def get_all_content():
    db = conn()
    cursor = db.cursor()

    cursor.execute("SELECT identifier, title, content FROM content")
    all_results = cursor.fetchall()
    content_dict = {
       row[0]: {
          "title": row[1],
          "content": row[2],
       }
       for row in all_results
    }
    return content_dict


def update_content(identifier: str, new_content: str):
    db = conn()
    cursor = db.cursor()

    if not identifier or not new_content:
        raise ValueError("Identifier ou new_content não podem ser vazios.")

    # fix bug on html SCEditor that sends extra <p>
    if identifier in ('horario', 'endereco'):
        new_content = new_content.lstrip("<p>\n\t").rstrip("\n</p>")

    try:
        cursor.execute(
            """UPDATE content SET content = ? WHERE identifier = ? """,
            (new_content, identifier)
        )
        db.commit()
        db.close()

    except Exception as e:
        print(f"Erro ao atualizar o conteúdo: {str(e)}")
        raise


def get_user(username):
    db = conn()
    cursor = db.cursor()
    cursor.execute("""\
        SELECT username, password FROM users WHERE username = ?""",
        (username,)
    )
    user = cursor.fetchone()
    db.close()
    if user:
        return dict(zip(("username", "password"), user))


def get_all_emails():
    db = conn()
    cursor = db.cursor()

    cursor.execute("SELECT * FROM contact ORDER by created DESC")
    all_results = cursor.fetchall()
    headers = "id name email phone date message created".split()
    db.close()

    return [
       dict(zip(headers, row))
       for row in all_results
    ]


def save_email(name: str, email: str, phone: str, date: str, message: str):
    db = conn()
    cursor = db.cursor()
    current_time = datetime.now()
    if date:
        date = datetime.strptime(date, "%Y-%m-%d")

    cursor.execute(
       """
       INSERT INTO contact (name, email, phone, date, message, created)
       VALUES (?, ?, ?, ?, ?, ?)
       """,
       [name, email, phone, date, message, current_time]
    )
    db.commit()
    db.close()
