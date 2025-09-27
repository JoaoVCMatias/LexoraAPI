from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base
from sqlalchemy import Identity

class Questao(Base):
    __tablename__ = "questao"

    idquestao = Column(Integer, primary_key=True, server_default=Identity(start=1))
    json = Column(String(100), nullable=False)
    idobjetivo = Column(Integer, ForeignKey("objetivo.idobjetivo"), nullable=False)
    idtipoquestao = Column(Integer, ForeignKey("tipo_questao.idtipoquestao"), nullable=False)
    nivel = Column(Integer, nullable=False)
    caminhoarquivo = Column(String(100))
