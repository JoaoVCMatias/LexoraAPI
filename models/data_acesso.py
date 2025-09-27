from sqlalchemy import Column, Integer, ForeignKey, DateTime
from database import Base
from sqlalchemy import Identity

class DataAcesso(Base):
    __tablename__ = "data_acesso"

    id_data_acesso = Column(Integer, primary_key=True, server_default=Identity(start=1))
    data_acesso = Column(DateTime)
    id_usuario = Column(Integer, ForeignKey("usuario.id_usuario"), nullable=False), 
