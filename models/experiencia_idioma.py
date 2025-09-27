from sqlalchemy import Column, Integer, String
from database import Base
from sqlalchemy import Identity

class ExperienciaIdioma(Base):
    __tablename__ = "experiencia_idioma"

    id_experiencia_idioma = Column(Integer, primary_key=True, server_default=Identity(start=1))
    descricao_experiencia_idioma = Column(String(45), nullable=False)
