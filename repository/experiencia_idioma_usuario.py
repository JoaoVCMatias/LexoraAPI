from sqlalchemy.orm import Session
from models import ExperienciaIdiomaUsuario

class ExperienciaIdiomaUsuarioRepository:
    def __init__(self, db: Session):
        self.db = db
    
    def pesquisar_experiencia_idioma_usuario(self, id_usuario):
        experiencia_cadastrada = self.db.query(ExperienciaIdiomaUsuario).filter(ExperienciaIdiomaUsuario.id_usuario == id_usuario).first()
        return experiencia_cadastrada
    
    def inserir_experiencia_idioma_usuario(self, experiencia_idioma_usuario: ExperienciaIdiomaUsuario):
        self.db.add(experiencia_idioma_usuario)
        self.db.commit()
        self.db.refresh(experiencia_idioma_usuario)
    
    def alterar_experiencia_idioma_usuario(self, id_usuario: int, id_idioma: int, id_experiencia_idioma: int):
        experiencia_cadastrada = self.db.query(ExperienciaIdiomaUsuario).filter(ExperienciaIdiomaUsuario.id_usuario == id_usuario and ExperienciaIdiomaUsuario.id_idioma == id_idioma).first()
        experiencia_cadastrada.id_experiencia_idioma = id_experiencia_idioma
        self.db.commit()
        self.db.refresh(experiencia_cadastrada)

