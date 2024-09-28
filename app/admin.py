from app.db import conn


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
