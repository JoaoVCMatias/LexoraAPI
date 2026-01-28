from sqlalchemy.orm import Session
from repository.objetivo_usuario import ObjetivoUsuarioRepository
from models import ObjetivoUsuario
from datetime import date
class ObjetivoUsuarioService:

    def __init__(self, db: Session):
        self.db = db

    def cadastrar_objetivo_usuario(self, id_usuario: int, id_objetivo: int):
        data_atual = date.today()
        objetivo_usuario = ObjetivoUsuario(id_usuario = id_usuario, id_objetivo = id_objetivo, data_criacao = data_atual, ativo = 1)
        objetivo_usuario_repository = ObjetivoUsuarioRepository(self.db)
        objetivo_usuario_repository.inserir_objetivo_usuario(objetivo_usuario)
    
    def deletar_objetivo_usuario(self, id_objetivo_usuario: int):
        data_atual = date.today()
        objetivo_usuario_repository = ObjetivoUsuarioRepository(self.db)
        objetivo_usuario_repository.deletar_objetivo_usuario(id_objetivo_usuario, data_atual)