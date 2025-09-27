from sqlalchemy import Column, Integer, String
from database import Base
from sqlalchemy import Identity

class Sexo(Base):
    __tablename__ = "sexo"

    idsexo = Column(Integer, primary_key=True, server_default=Identity(start=1))
    descricaosexo = Column(String(20), nullable=False)
    siglasexo = Column(String(2), nullable=False)
