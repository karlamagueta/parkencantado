from sqlite3 import connect

def conn():
    return connect("app/database.db")

def initialize_database():
    db = conn()
    cursor = db.cursor()

    cursor.execute(
        """\
        CREATE TABLE IF NOT EXISTS termos_e_condicoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title VARCHAR UNIQUE NOT NULL,
            content VARCHAR NOT NULL
        );
        """
    )


    cursor.execute("SELECT * FROM termos_e_condicoes")
    if cursor.fetchone() is None:
        cursor.execute(
            """
            INSERT INTO termos_e_condicoes (title, content)
            VALUES (
                "Termos de Uso",
                "Estes são os termos e condições do parque"
            );
            """
        )

    cursor.execute(
        """\
        CREATE TABLE IF NOT EXISTS sobre_o_parque (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title VARCHAR UNIQUE NOT NULL,
            content VARCHAR NOT NULL
        );
        """
    )


    cursor.execute("SELECT * FROM sobre_o_parque")
    if cursor.fetchone() is None:
        cursor.execute(
            """
            INSERT INTO sobre_o_parque (title, content)
            VALUES (
                "Sobre o Parque",
                "Estas são as informações sobre o parque"
            );
            """
        )

    db.commit()
    db.close()


initialize_database()
