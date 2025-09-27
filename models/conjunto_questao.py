from sqlalchemy import Column, Integer, ForeignKey, DateTime
from database import Base
from sqlalchemy import Identity

class ConjuntoQuestao(Base):
    __tablename__ = "conjunto_questao"

    id_conjunto_questao = Column(Integer, primary_key=True, server_default=Identity(start=1))
    id_usuario = Column(Integer, ForeignKey("usuario.id_usuario"), nullable=False)
    data_criacao = Column(DateTime, nullable=False)
    data_conclusao = Column(DateTime)
