from sqlalchemy import Column, Integer, ForeignKey
from database import Base
from sqlalchemy import Identity

class ExperienciaIdiomaUsuario(Base):
    __tablename__ = "experiencia_idioma_usuario"

    id_experiencia_idioma_usuario = Column(Integer, primary_key=True, server_default=Identity(start=1))
    id_usuario = Column(Integer, ForeignKey("usuario.id_usuario"), nullable=False)
    id_idioma = Column(Integer, ForeignKey("idioma.id_idioma"), nullable=False)
    id_experiencia_idioma = Column(Integer, ForeignKey("experiencia_idioma.id_experiencia_idioma"), nullable=False)
