from sqlalchemy.orm import Session
from models import ExperienciaIdiomaUsuario

class ExperienciaIdiomaUsuarioRepository:
    def __init__(self, db: Session):
        self.db = db
    
    def inserir_experiencia_idioma_usuario(self, experiencia_idioma_usuario: ExperienciaIdiomaUsuario):
        self.db.add(experiencia_idioma_usuario)
        self.db.commit()
        self.db.refresh(experiencia_idioma_usuario)
    
    def alterar_experiencia_idioma_usuario(self, id_experienca_idioma_usuario, id_experiencia_idioma: int):
        experiencia_cadastrada = self.db.query(ExperienciaIdiomaUsuario).filter(ExperienciaIdiomaUsuario.id_experiencia_idioma_usuario == id_experienca_idioma_usuario).first()
        experiencia_cadastrada.id_experiencia_idioma = id_experiencia_idioma

