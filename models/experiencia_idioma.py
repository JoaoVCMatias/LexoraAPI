from sqlalchemy import Column, Integer, String
from database import Base
from sqlalchemy import Identity

class ExperienciaIdioma(Base):
    __tablename__ = "experiencia_idioma"

    idexperienciaidioma = Column(Integer, primary_key=True, server_default=Identity(start=1))
    descricaoexperienciaidioma = Column(String(45), nullable=False)
