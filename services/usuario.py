from fastapi import  HTTPException
from sqlalchemy.orm import Session
from schemas.usuario import UsuarioCreate
from models import Usuario
from datetime import date
from sqlalchemy.orm import Session
from .validacao import ValidacaoService

class UsuarioService:
    def __init__(self, db: Session):
        self.db = db

    def validar_dados_usuario(self, usuario: UsuarioCreate):
        validacaoEmail = ValidacaoService(self.db)
        email_validacao = validacaoEmail.Validacao_Email(usuario.email)
        if email_validacao == False:
            raise HTTPException(status_code=422, detail="Email já cadastrado no sistema.")
        pass

    def Cadastrar_Usuario(self, usuario: UsuarioCreate):
        self.validar_dados_usuario(usuario)
        data_atual = date.today()
        novo_usuario = Usuario(nome = usuario.nome, email = usuario.email, senha = usuario.senha, cadastro_completo = 0, data_ultimo_acesso = data_atual, data_criacao = data_atual, ativo = False)
        self.db.add(novo_usuario)
        self.db.commit()
        self.db.refresh(novo_usuario)
        return 1
    
    