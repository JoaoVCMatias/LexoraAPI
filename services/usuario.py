from fastapi import  HTTPException
from sqlalchemy.orm import Session
from schemas.usuario import UsuarioCreate, UsuarioInfosCreate ,UsuarioAutentication
from schemas.usuario_token import UsuarioTokenCreate
from models import Usuario
from datetime import date
from .validacao import ValidacaoService
from .senha import SenhaService
from .autenticacao import AutenticacaoService
from repository.usuario import UsuarioRepository

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
    
    def cadastrar_usuario(self, usuario: UsuarioCreate):
        usuario_repository = UsuarioRepository(self.db)
        self.validar_dados_usuario(usuario)
        data_atual = date.today()
        hash_senha = self.gerar_hash_senha(usuario.senha)
        novo_usuario = Usuario(nome = usuario.nome, email = usuario.email, senha = hash_senha, cadastro_completo = 0, data_ultimo_acesso = data_atual, data_criacao = data_atual, ativo = False)
        usuario_repository.inserir_usuario(novo_usuario)
        token = self.gerar_token(novo_usuario.id_usuario)
        self.salvar_token(novo_usuario, token)
        return token

    def alterar_usuario_informacao(self, id_usuario, usuario: UsuarioInfosCreate):
        usuario_repositoy = UsuarioRepository(self.db)
        usuario_cadastrado = usuario_repositoy.buscar_usuario_por_id(id_usuario)
        if usuario_cadastrado is None:
            raise HTTPException(status_code=401, detail="Usuário não encontrado.")
        usuario_repositoy.alterar_informacoes_usuario(id_usuario, usuario)

  
            
        
        
    
    #def buscar_usuario_token(self, token: str):
    #    id_usuario = AutenticacaoService.token_to_id_usuario(token)
    #    self.db.query(Usuario)
    #    self.db.commit()
    #    token = self.gerar_token(novo_usuario.id_usuario)
    #    self.salvar_token(novo_usuario, token)
    #    return token
    
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
       

    
    