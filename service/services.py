from repository.dao_entity import DAOEntity
from entities.entity import Entity

class Services:

    def __init__(self, repository):
        self.repository = repository

    def create(self, titulo: str, artista: str, ano: int, descricao: str = "") -> int:
        titulo = titulo.strip()
        
        if not titulo:
            raise ValueError("O título do disco é obrigatório.")
        
        if not artista:
            raise ValueError("O artista do disco é obrigatório.")
        
        if type(ano) is not int:
            raise ValueError("O ano do disco deve ser um número inteiro.")
        
        disco = Entity(
            titulo=titulo,
            artista=artista,
            ano=ano,
            descricao_disco=descricao,
            )
        return self.repository.create(disco)

    def list(self):
        return self.repository.find_all()

    def get(self, disco_id: int) -> Entity | None:
        return self.repository.find_by_id(disco_id)

    def update(self, task_id, title, description):
        pass

    def delete(self, task_id):
        pass