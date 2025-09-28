from fastapi import Depends
from sqlalchemy.orm import Session
from schemas.usuario import UsuarioCreate
from database import get_db
from models import Usuario
from datetime import date
from sqlalchemy.orm import Session

class UsuarioService:
    def __init__(self, db: Session):
        self.db = db

    def Cadastrar_Usuario(self, usuario: UsuarioCreate):
        data_atual = date.today()
        novo_usuario = Usuario(nome = usuario.nome, email = usuario.email, senha = usuario.senha, cadastro_completo = 0, data_ultimo_acesso = data_atual, data_criacao = data_atual)
        self.db.add(novo_usuario)
        self.db.commit()
        self.db.refresh(novo_usuario)
        return 1