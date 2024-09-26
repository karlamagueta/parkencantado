from sqlite3 import connect

def conn():
    return connect("app/database.db")

def initialize_database():
    db = conn()
    cursor = db.cursor()

    cursor.execute(
        """\
        CREATE TABLE IF NOT EXISTS content (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            identifier VARCHAR UNIQUE NOT NULL,
            title VARCHAR NOT NULL,
            content VARCHAR NOT NULL
        );
        """
    )


    cursor.execute("SELECT * FROM content")
    if cursor.fetchone() is None:
        cursor.executemany(
            """
            INSERT INTO content (identifier, title, content)
            VALUES (?, ?, ?)
            """,
            [
                ("termos", "Termos de Uso", "Estes são os termos e condições do parque"),
                ("sobre", "Sobre o Parque", "Esta é a seção sobre o parque.")
            ]
        )

    db.commit()
    db.close()


initialize_database()
