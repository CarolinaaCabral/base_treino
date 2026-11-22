class Entity:
    def __init__(
        self,
        titulo: str,
        artista: str,
        ano: int,
        disco_id: int | None = None,
        descricao_disco: str = "",
        ouvido: bool = False,
        ):
        self.id = disco_id
        self.titulo = titulo
        self.artista = artista
        self.ano = ano
        self.descricao = descricao_disco
        self.ouvido = ouvido
        
        