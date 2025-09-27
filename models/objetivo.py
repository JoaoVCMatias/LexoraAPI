from sqlalchemy import Column, Integer, String
from database import Base
from sqlalchemy import Identity

class Objetivo(Base):
    __tablename__ = "objetivo"

    idobjetivo = Column(Integer, primary_key=True, server_default=Identity(start=1))
    descricaoobjetivo = Column(String(45), nullable=False)
