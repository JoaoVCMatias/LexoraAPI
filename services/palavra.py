from requests import Session

from repository.objetivo_usuario import ObjetivoUsuarioRepository
from repository.palavra import PalavraRepository


class PalavraService:
    def __init__(self, db: Session):
        self.db = db

    def buscar_todas_palavras(self) -> list:
        palavra_repository = PalavraRepository(self.db)
        palavras = palavra_repository.buscar_todas_palavras()
        return palavras
        
    def busca_palavras_por_objetivo_usuario(self, id_usuario: int):
        objetivo_usuario_repository = ObjetivoUsuarioRepository(self.db)
        palavra_repository = PalavraRepository(self.db)
        objetivo_palavras = objetivo_usuario_repository.objetivo_usuario_palavras(id_usuario)

        for objetivo in objetivo_palavras:
            palavras_objetivo = palavra_repository.busca_palavras_por_objetivo_usuario(objetivo.id_objetivo_usuario)
            objetivo.palavras = palavras_objetivo

        return objetivo_palavras
    
    def buscar_palavra_por_id(self, id_palavra: int):
        palavra_repository = PalavraRepository(self.db)
        palavra = palavra_repository.buscar_palavra_por_id(id_palavra)
        return palavra
    
    def buscar_palavras_por_nivel_cerf(self, nivel_cerf: str) -> list:
        palavra_repository = PalavraRepository(self.db)
        palavras = palavra_repository.busca_palavras_por_cefr(nivel_cerf)
        return palavras
    
    def buscar_palavras_por_descricao(self, descricao_palavra: str) -> list:
        palavra_repository = PalavraRepository(self.db)
        palavras = palavra_repository.busca_palavra_por_descricao(descricao_palavra)
        return palavras