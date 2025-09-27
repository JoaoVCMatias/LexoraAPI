from sqlalchemy import Column, Integer, String
from database import Base
from sqlalchemy import Identity

class Disponibilidade(Base):
    __tablename__ = "disponibilidade"

    id_disponibilidade = Column(Integer, primary_key=True, server_default=Identity(start=1))
    descricao_disponibilidade = Column(String(50), nullable=False)
