from sqlalchemy import Column, Integer, ForeignKey
from database import Base
from sqlalchemy import Identity

class NivelQuestaoUsuario(Base):
    __tablename__ = "nivel_questao_usuario"

    id_nivel_questao_usuario = Column(Integer, primary_key=True, server_default=Identity(start=1))
    nivel = Column(Integer, nullable=False)
    id_usuario = Column(Integer, ForeignKey("usuario.id_usuario"), nullable=False)
    id_questao = Column(Integer, ForeignKey("questao.id_questao"), nullable=False)
