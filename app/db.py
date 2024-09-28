from sqlite3 import connect
from .config import settings


def conn():
    return connect(settings.database.path)

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
                ("regulamento", "Termos de Uso", "Estes são os termos e condições do parque"),
                ("sobre", "Sobre o Parque", "Esta é a seção sobre o parque."),
                ("horario", "Horários","Quarta a sexta-feira: 14h - 19h*<br>Sábado e Domingo: 10h - 19h*<br>Folga semanal: Segundas e Terças-feira*"),
                ("endereco", "Endereço", "R. Estrada da Igreja 2310, 4925-573 Perre<br>Viana do Castelo, Portugal")
            ]
        )

    db.commit()
    db.close()


initialize_database()
