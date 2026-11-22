from database.connection import get_connection


def install():
    connection = get_connection()

    try:
        connection.execute("BEGIN IMMEDIATE")

        connection.execute("""
            CREATE TABLE IF NOT EXISTS discos (
                id INTEGER PRIMARY KEY,
                titulo TEXT NOT NULL,
                artista TEXT NOT NULL,
                ano INTEGER NOT NULL,
                descricao TEXT NOT NULL DEFAULT '',
                ouvido BOOLEAN NOT NULL DEFAULT FALSE
            )
        """)

        versao = connection.execute("PRAGMA user_version").fetchone()[0]

        if versao == 0:
            connection.executemany(
                """
                INSERT INTO discos (titulo, artista, ano, descricao)
                VALUES (?, ?, ?, ?)
                """,
                [
                    ("Toxicity", "System of a Down", 2001, "Álbum de rock"),
                    ("Mezmerize", "System of a Down", 2005, "Álbum de rock"),
                    ("Californication", "Red Hot Chili Peppers", 1999, "Álbum de Rock"),
                    
                ],
            )
            
            connection.execute(
                "INSERT INTO discos (titulo, artista, ano, descricao, ouvido) VALUES (?, ?, ?, ?, ?)",
                ("Demon Days", "Gorillaz", 2005, "Álbum de Rock Alternativo", True)
            )

            connection.execute("PRAGMA user_version = 1")

        connection.commit()

    finally:
        connection.close()


if __name__ == "__main__":
    install()
    print("Banco de dados instalado com sucesso.")