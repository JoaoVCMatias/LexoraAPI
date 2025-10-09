from sqlalchemy import Column, Integer, String
from database import Base
from sqlalchemy import Identity

class Palavra(Base):
    __tablename__ = "palavra"

    id_palavra = Column(Integer, primary_key=True, server_default=Identity(start=1))
    descricao_palavra = Column(String(45), nullable=False)
    descricao_palavra_traducao = Column(String(45), nullable=True)
    CEFR = Column(String(2), nullable=False)
