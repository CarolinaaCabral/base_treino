import os
import sqlite3

def get_connection():
    caminho = os.path.join("database", "banco.db")
    conn = sqlite3.connect(caminho)
    conn.row_factory = sqlite3.Row
    return conn
