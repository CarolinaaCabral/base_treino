from repository.dao_entity import DAOEntity
from entities.entity import Entity

class Services:

    def __init__(self, repository):
        self.repository = repository

    def create(self, titulo: str, artista: str, ano: int, descricao: str = "") -> int:
        titulo, artista = self._validar_dados_disco(titulo, artista, ano)
        
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

    def update(
        self,
        disco_id: int,
        titulo: str,
        artista: str,
        ano: int,
        descricao: str = "",
        ) -> bool:
        titulo, artista = self._validar_dados_disco(titulo, artista, ano)
        
        disco = Entity(
            disco_id=disco_id,
            titulo=titulo,
            artista=artista,
            ano=ano,
            descricao_disco=descricao,
            )
        return self.repository.update(disco)
    
    def _validar_dados_disco(
        self, titulo: str, artista: str, ano: int
        ) -> tuple[str, str]:
        titulo = titulo.strip()
        artista = artista.strip()
        
        if not titulo:
            raise ValueError("O título do disco é obrigatório.")
        
        if not artista:
            raise ValueError("O artista do disco é obrigatório.")
        
        if type(ano) is not int:
            raise ValueError("O ano dever ser um número inteiro.")
        return titulo, artista
    

    def delete(self, disco_id):
        return self.repository.delete(disco_id)
    
    def marcar_como_ouvido(self, disco_id: int) -> bool:
        return self.repository.set_ouvido(disco_id, True)
        
    def marcar_como_nao_ouvido(self, disco_id: int) -> bool:
        return self.repository.set_ouvido(disco_id, False)