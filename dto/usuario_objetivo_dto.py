class UsuarioObjetivoDto:
    def __init__(self, id_objetivo_usuario: int, id_objetivo: int, descricao_objetivo: str):
        self.id_objetivo_usuario = id_objetivo_usuario
        self.id_objetivo = id_objetivo
        self.descricao_objetivo = descricao_objetivo