from sqlalchemy import Column, Integer, ForeignKey, DateTime
from database import Base
from sqlalchemy import Identity

class DataAcesso(Base):
    __tablename__ = "data_acesso"

    iddataacesso = Column(Integer, primary_key=True, server_default=Identity(start=1))
    dataacesso = Column(DateTime)
    idusuario = Column(Integer, ForeignKey("usuario.idusuario"), nullable=False), 
