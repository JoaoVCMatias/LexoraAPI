from sqlalchemy.orm import Session
from repository.experiencia_idioma_usuario import ExperienciaIdiomaUsuarioRepository
from models.experiencia_idioma_usuario import ExperienciaIdiomaUsuario

class ExperienciaIdiomaUsuarioService:

    def __init__(self, db: Session):
        self.db = db
    
    def pesquisar_experiencia_idioma_usuario(self, id_usuario: int):
        experienciaIdiomaUsuarioRepository = ExperienciaIdiomaUsuarioRepository(self.db)
        experiencia_idioma_usuario = experienciaIdiomaUsuarioRepository.pesquisar_experiencia_idioma_usuario(id_usuario)
        return experiencia_idioma_usuario

    def cadastrar_experiencia_idioma_usuario(self, id_idioma: int, id_usuario: int, id_experiencia_idioma: int):
        experiencia = ExperienciaIdiomaUsuario(id_idioma = id_idioma, id_usuario = id_usuario, id_experiencia_idioma = id_experiencia_idioma)
        experienciaIdiomaUsuarioRepository = ExperienciaIdiomaUsuarioRepository(self.db)
        experienciaIdiomaUsuarioRepository.inserir_experiencia_idioma_usuario(experiencia)

    def alterar_experiencia_idioma_usuario(self, id_idioma: int, id_usuario: int, id_experiencia_idioma):
        experienciaIdiomaUsuarioRepository = ExperienciaIdiomaUsuarioRepository(self.db)
        experienciaIdiomaUsuarioRepository.alterar_experiencia_idioma_usuario(id_usuario, id_idioma, id_experiencia_idioma)