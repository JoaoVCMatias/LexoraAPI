from sqlalchemy import Column, Integer, ForeignKey, DateTime
from database import Base
from sqlalchemy import Identity

class ConjuntoQuestao(Base):
    __tablename__ = "conjunto_questao"

    idconjuntoquestao = Column(Integer, primary_key=True, server_default=Identity(start=1))
    idusuario = Column(Integer, ForeignKey("usuario.idusuario"), nullable=False)
    datacriacao = Column(DateTime, nullable=False)
    dataconclusao = Column(DateTime)
