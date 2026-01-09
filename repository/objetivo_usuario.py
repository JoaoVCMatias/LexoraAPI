from sqlalchemy.orm import Session
from models import ObjetivoUsuario
from datetime import date

class ObjetivoUsuarioRepository:

    def __init__(self, db: Session):
        self.db = db

    def inserir_objetivo_usuario(self, objetivo_usuario: ObjetivoUsuario):
        self.db.add(objetivo_usuario)
        self.db.commit()
        self.db.refresh(objetivo_usuario)
    
    def pesquisar_objetivo_usuario(self, id_usuario: int):
        objetivo_usuario = self.db.query(ObjetivoUsuario).filter(ObjetivoUsuario.id_usuario == id_usuario).first()
        return objetivo_usuario
    
    def pesquisar_objetivos_usuario(self, id_usuario: int):
        objetivo_usuario = self.db.query(ObjetivoUsuario).filter(ObjetivoUsuario.id_usuario == id_usuario).all()
        return objetivo_usuario

    def deletar_objetivo_usuario(self, id_objetivo_usuario, data_atual: date):
        objetivo_cadastrada = self.db.query(ObjetivoUsuario).filter(ObjetivoUsuario.id_objetivo_usuario == id_objetivo_usuario).first()
        objetivo_cadastrada.data_exclusao = data_atual
        objetivo_cadastrada.ativo = 0
        self.db.commit()
        self.db.refresh(objetivo_cadastrada)
