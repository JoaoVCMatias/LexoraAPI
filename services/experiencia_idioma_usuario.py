from sqlalchemy.orm import Session
from repository.experiencia_idioma_usuario import ExperienciaIdiomaUsuarioRepository
from models.experiencia_idioma_usuario import ExperienciaIdiomaUsuario

class ExperienciaIdiomaUsuarioService:

    def __init__(self, db: Session):
        self.db = db
    
    def cadastrar_experiencia_idioma_usuario(self, id_idioma: int, id_usuario: int, id_experienci_idioma):
        experiencia =  ExperienciaIdiomaUsuario(id_idioma = id_idioma, id_usuario = id_usuario, id_experienci_idioma = id_experienci_idioma)
        ExperienciaIdiomaUsuarioRepository.inserir_experiencia_idioma_usuario(experiencia)