from sqlalchemy import text
from sqlalchemy.orm import Session
from models import ObjetivoUsuario
from datetime import date

from models.objetivo import Objetivo
from schemas.palavra import ObjetivoPalavras

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
    
    def objetivo_usuario_palavras(self, id_usuario: int) -> list[ObjetivoPalavras]:
        objetivo_usuario = self.db.execute(text("""
            SELECT 
                a.id_objetivo_usuario,
                b.id_objetivo,
                b.descricao_objetivo
            FROM objetivo_usuario a
            JOIN objetivo b ON a.id_objetivo = b.id_objetivo
            WHERE a.id_usuario = :id_usuario
        """), {"id_usuario": id_usuario}).all()

        objetivos = []
        for objetivo in objetivo_usuario:
            objetivos.append(
                ObjetivoPalavras(
                    id_objetivo_usuario=objetivo.id_objetivo_usuario,
                    id_objetivo=objetivo.id_objetivo,
                    descricao_objetivo=objetivo.descricao_objetivo,
                    palavras=[]
                )
            )

        return objetivos


    def deletar_objetivo_usuario(self, id_objetivo_usuario, data_atual: date):
        objetivo_cadastrada = self.db.query(ObjetivoUsuario).filter(ObjetivoUsuario.id_objetivo_usuario == id_objetivo_usuario).first()
        objetivo_cadastrada.data_exclusao = data_atual
        objetivo_cadastrada.ativo = 0
        self.db.commit()
        self.db.refresh(objetivo_cadastrada)
