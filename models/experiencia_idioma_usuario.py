from sqlalchemy import Column, Integer, ForeignKey
from database import Base
from sqlalchemy import Identity

class ExperienciaIdiomaUsuario(Base):
    __tablename__ = "experiencia_idioma_usuario"

    idexperienciaidiomausuario = Column(Integer, primary_key=True, server_default=Identity(start=1))
    idusuario = Column(Integer, ForeignKey("usuario.idusuario"), nullable=False)
    ididioma = Column(Integer, ForeignKey("idioma.ididioma"), nullable=False)
    idexperienciaidioma = Column(Integer, ForeignKey("experiencia_idioma.idexperienciaidioma"), nullable=False)
