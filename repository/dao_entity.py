from database.connection import get_connection

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
        # Consultar todas as entidades
        pass

    def find_by_id(self, task_id):
        # Consultar pelo ID
        pass

    def update(self, task):
        # Atualizar
        pass

    def delete(self, task_id):
        # Excluir
        pass