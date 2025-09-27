from sqlalchemy import Column, Integer, ForeignKey
from database import Base
from sqlalchemy import Identity

class NivelQuestaoUsuario(Base):
    __tablename__ = "nivel_questao_usuario"

    idnivelquestaousuario = Column(Integer, primary_key=True, server_default=Identity(start=1))
    nivel = Column(Integer, nullable=False)
    idusuario = Column(Integer, ForeignKey("usuario.idusuario"), nullable=False)
    idquestao = Column(Integer, ForeignKey("questao.idquestao"), nullable=False)
