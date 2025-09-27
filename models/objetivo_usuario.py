from sqlalchemy import Column, Integer, ForeignKey, DateTime, Boolean, String
from database import Base
from sqlalchemy import Identity

class ObjetivoUsuario(Base):
    __tablename__ = "objetivo_usuario"

    idobjetivousuario = Column(Integer, primary_key=True, server_default=Identity(start=1))
    idusuario = Column(Integer, ForeignKey("usuario.idusuario"), nullable=False)
    idobjetivo = Column(Integer, ForeignKey("objetivo.idobjetivo"), nullable=False)
    datacriacao = Column(DateTime, nullable=False)
    ativo = Column(Boolean)
    dataexclusao = Column(String(45))
