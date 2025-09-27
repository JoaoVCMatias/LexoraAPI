from sqlalchemy import Column, Integer, String
from database import Base
from sqlalchemy import Identity

class TipoQuestao(Base):
    __tablename__ = "tipo_questao"

    idtipoquestao = Column(Integer, primary_key=True, server_default=Identity(start=1))
    descricaotipoquestao = Column(String(50), nullable=False)
