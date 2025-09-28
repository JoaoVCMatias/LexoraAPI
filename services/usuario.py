from fastapi import  HTTPException
from sqlalchemy.orm import Session
from schemas.usuario import UsuarioCreate, UsuarioAutentication
from schemas.usuario_token import UsuarioTokenCreate
from models import Usuario
from datetime import date
from sqlalchemy.orm import Session
from .validacao import ValidacaoService
from .senha import SenhaService
from .autenticacao import AutenticacaoService
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

    def salvar_token(self, usuario: Usuario, token: str):
        usuario_token = UsuarioTokenCreate(id_usuario= usuario.id_usuario, token= token)
        autenticacaoService = AutenticacaoService(self.db)
        autenticacaoService.salvar_token(usuario_token)
        print("Token salvo")

    @staticmethod
    def gerar_token(id_usuario: int):
        return AutenticacaoService.gerar_token(id_usuario)
    
    def cadastrar_Usuario(self, usuario: UsuarioCreate):
        self.validar_dados_usuario(usuario)
        data_atual = date.today()
        hash_senha = self.gerar_hash_senha(usuario.senha)
        novo_usuario = Usuario(nome = usuario.nome, email = usuario.email, senha = hash_senha, cadastro_completo = 0, data_ultimo_acesso = data_atual, data_criacao = data_atual, ativo = False)
        self.db.add(novo_usuario)
        self.db.commit()
        self.db.refresh(novo_usuario)
        print("Log: Usuario cadastrado")
        token = self.gerar_token(novo_usuario.id_usuario)
        self.salvar_token(novo_usuario, token)
        return token
    
    def validar_autenticacao(self, usuario : UsuarioAutentication):
        usuarioCadastrado = self.db.query(Usuario).filter(Usuario.email == usuario.email).first()
        senhaService = SenhaService()

        comparacaoSenha = senhaService.Compare(usuario.senha, usuarioCadastrado.senha)
        if comparacaoSenha == False:
            raise HTTPException(status_code=401, detail="Credenciais inválidas. Verifique seu e-mail e senha.")
        
        autenticacao = AutenticacaoService(self.db)

        autenticacao.delata_token_por_id(usuarioCadastrado.id_usuario)
        token = self.gerar_token(usuarioCadastrado.id_usuario)
        self.salvar_token(usuarioCadastrado, token)
        return token
       

    
    