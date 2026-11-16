from database.connection import get_connection


def install():
    connection = get_connection()

    try:
        connection.execute("""""")

        connection.commit()

    finally:
        connection.close()


if __name__ == "__main__":
    install()
    print("Banco de dados instalado com sucesso.")