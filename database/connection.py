import os
import sqlite3


DATABASE_PATH = BASE_DIR / "database" / "banco.db"

def get_connection():
    DATABASE_PATH.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row

    return connection
