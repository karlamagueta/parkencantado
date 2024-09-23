from app.db import conn

def get_content(table, title):
    db = conn()
    cursor = db.cursor()

    results = cursor.execute(f"SELECT content FROM {table} WHERE title = ?", (title,))
    content = [result for result in results]

    db.close()
    return title, content[0][0]
