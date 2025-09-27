from sqlalchemy import Column, Integer, ForeignKey, DateTime, Boolean, String
from database import Base
from sqlalchemy import Identity

class ObjetivoUsuario(Base):
    __tablename__ = "objetivo_usuario"

    id_objetivo_usuario = Column(Integer, primary_key=True, server_default=Identity(start=1))
    id_usuario = Column(Integer, ForeignKey("usuario.id_usuario"), nullable=False)
    id_objetivo = Column(Integer, ForeignKey("objetivo.id_objetivo"), nullable=False)
    data_criacao = Column(DateTime, nullable=False)
    ativo = Column(Boolean)
    data_exclusao = Column(String(45))
