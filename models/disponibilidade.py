from sqlalchemy import Column, Integer, String
from database import Base
from sqlalchemy import Identity

class Disponibilidade(Base):
    __tablename__ = "disponibilidade"

    iddisponibilidade = Column(Integer, primary_key=True, server_default=Identity(start=1))
    descricaodisponibilidade = Column(String(50), nullable=False)
