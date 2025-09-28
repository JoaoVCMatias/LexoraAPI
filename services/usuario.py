from fastapi import  HTTPException
from sqlalchemy.orm import Session
from schemas.usuario import UsuarioCreate, UsuarioAutentication
from models import Usuario
from datetime import date
from sqlalchemy.orm import Session
from .validacao import ValidacaoService
from .senha import SenhaService
from sqlalchemy import exists

class UsuarioService:
    def __init__(self, db: Session):
        self.db = db

    def validar_dados_usuario(self, usuario: UsuarioCreate):
        validacaoEmail = ValidacaoService(self.db)
        email_validacao = validacaoEmail.Validacao_Email(usuario.email)
        if email_validacao == False:
            raise HTTPException(status_code=422, detail="Email já cadastrado no sistema.")
        pass
    
    @staticmethod
    def gerar_hash_senha(senha : str) -> bytes:
        senhaService = SenhaService()
        return senhaService.ToHash(senha)

    def cadastrar_Usuario(self, usuario: UsuarioCreate):
        self.validar_dados_usuario(usuario)
        data_atual = date.today()
        hash_senha = self.gerar_hash_senha(usuario.senha)
        novo_usuario = Usuario(nome = usuario.nome, email = usuario.email, senha = hash_senha, cadastro_completo = 0, data_ultimo_acesso = data_atual, data_criacao = data_atual, ativo = False)
        self.db.add(novo_usuario)
        self.db.commit()
        self.db.refresh(novo_usuario)
        print("Log: Usuario cadastrado")
        return 1
    
    def validar_autenticacao(self, usuario : UsuarioAutentication):
        usuarioCadastrado = self.db.query(Usuario).filter(Usuario.email == usuario.email).first()
        senhaService = SenhaService()

        comparacaoSenha = senhaService.Compare(usuario.senha, usuarioCadastrado.senha)

        return comparacaoSenha

    
    