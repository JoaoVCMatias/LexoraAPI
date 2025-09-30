from sqlalchemy.orm import Session
from models import Usuario
from schemas.usuario import UsuarioInfosCreate 

class UsuarioRepository:
    def __init__(self, db: Session):
        self.db = db
    
    def buscar_usuario_por_id(self, id_usuario: int):
        usuario = self.db.query(Usuario).filter(Usuario.id_usuario == id_usuario).first()
        return usuario
    
    def buscar_usuario_por_email(self, email: str):
        usuario = self.db.query(Usuario).filter(Usuario.email == email).first()
        return usuario
    
    def inserir_usuario(self, novo_usuario: Usuario):
        self.db.add(novo_usuario)
        self.db.commit()
        self.db.refresh(novo_usuario)
        print("Log: Usuario cadastrado")

    def alterar_informacoes_usuario(self, id_usuario: int, usuario_alteracao: UsuarioInfosCreate):
        usuario_cadastrado = self.db.query(Usuario).filter(Usuario.id_usuario == id_usuario).first()
        usuario_cadastrado.id_idiomamaterno = 1
        usuario_cadastrado.id_disponibilidade = usuario_alteracao.id_disponibilidade
        usuario_cadastrado.data_nascimento = usuario_alteracao.data_nascimento
        self.db.commit()
    
    def concluir_cadastro(self, id_usuario):
        usuario_cadastrado = self.db.query(Usuario).filter(Usuario.id_usuario == id_usuario).first()
        usuario_cadastrado.cadastro_completo = True
        self.db.commit()
    

