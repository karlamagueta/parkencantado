from app.db import conn


def get_all_content():
    db = conn()
    cursor = db.cursor()

    cursor.execute("SELECT identifier, title, content FROM content")
    all_results = cursor.fetchall()
    content_dict = [
        {"identifier": row[0], "title": row[1], "content": row[2]} for row in all_results
    ]

    return content_dict


def update_content(identifier: str, new_content: str):
    db = conn()
    cursor = db.cursor()

    if not identifier or not new_content:
        raise ValueError("Identifier ou new_content não podem ser vazios.")

    try:
        cursor.execute("""UPDATE content SET content = ? WHERE identifier = ? """,
        (new_content, identifier)
        )
        db.commit()
        db.close()

    except Exception as e:
        print(f"Erro ao atualizar o conteúdo: {str(e)}")
        raise
