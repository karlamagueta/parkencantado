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
