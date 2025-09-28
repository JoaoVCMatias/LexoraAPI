from sqlalchemy import Column, Integer, Text, ForeignKey
from database import Base
from sqlalchemy import Identity

class UsuarioToken(Base):
    __tablename__ = "usuario_token"

    id_usuario_token = Column(Integer, primary_key=True, server_default=Identity(start=1))
    id_usuario = Column(Integer, ForeignKey("usuario.id_usuario"), nullable=False)
    token = Column(Text, nullable=False)
