from .usuario_experiencia_idioma_dto import UsuarioExperienciaIdiomaDto
from .usuario_objetivo_dto import UsuarioObjetivoDto
class UsuarioInfoDto:
    usuario_experiencia_idioma: UsuarioExperienciaIdiomaDto
    usuario_objetivo: UsuarioObjetivoDto
    def __init__(self, id_usuario, nome, email, data_nascimento, id_disponibilidade, descricao_disponibilidade):
        self.id_usuario = id_usuario
        self.nome = nome
        self.email = email
        self.data_nascimento = data_nascimento
        self.id_disponibilidade = id_disponibilidade
        self.descricao_disponibilidade = descricao_disponibilidade