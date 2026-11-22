from database.connection import get_connection
from entities.entity import Entity

class DAOEntity:

    def create(self, disco):
        connection = get_connection()
        
        try:
            cursor = connection.execute(
                """
                INSERT INTO discos (titulo, artista, ano, descricao)
                VALUES (?, ?, ?, ?)
                """,
                (disco.titulo, disco.artista, disco.ano, disco.descricao),
                )
            
            connection.commit()
            return cursor.lastrowid
        finally:
            connection.close
            

    def find_all(self):
        connection = get_connection()
        
        try:
            cursor = connection.execute(
            """
            SELECT id, titulo, artista, ano, descricao, ouvido
            FROM discos
            ORDER BY id
            """
            )
            
            linhas = cursor.fetchall()
            
            return [
                Entity(
                    disco_id=linha["id"],
                    titulo=linha["titulo"],
                    artista=linha["artista"],
                    ano=linha["ano"],
                    descricao_disco=linha["descricao"],
                    ouvido=linha["ouvido"]
                    )
                for linha in linhas
                ]
        finally:
            connection.close()
            
    def find_by_id(self, disco_id):
        connection = get_connection()
        
        try:
            cursor = connection.execute(
                """
                SELECT id, titulo, artista, ano, descricao, ouvido
                FROM discos
                WHERE id = ?
                """,
                (disco_id,),
                )
            linha = cursor.fetchone()
            
            if linha is None:
                return None
            
            return Entity(
                disco_id=linha["id"],
                titulo=linha["titulo"],
                artista=linha["artista"],
                ano=linha["ano"],
                descricao_disco=linha["descricao"],
                ouvido=bool(linha["ouvido"]),
                )
        finally:
            connection.close()

    def update(self, task):
        # Atualizar
        pass

    def delete(self, task_id):
        # Excluir
        pass