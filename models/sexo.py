from sqlalchemy import Column, Integer, String
from database import Base
from sqlalchemy import Identity

class Sexo(Base):
    __tablename__ = "sexo"

    id_sexo = Column(Integer, primary_key=True, server_default=Identity(start=1))
    descricao_sexo = Column(String(20), nullable=False)
    sigla_sexo = Column(String(2), nullable=False)
