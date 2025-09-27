from sqlalchemy import Column, Integer, String
from database import Base
from sqlalchemy import Identity

class Idioma(Base):
    __tablename__ = "idioma"

    id_idioma = Column(Integer, primary_key=True, server_default=Identity(start=1))
    descricao_idioma = Column(String(50))
