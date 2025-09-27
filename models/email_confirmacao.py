from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base
from sqlalchemy import Identity

class EmailConfirmacao(Base):
    __tablename__ = "email_confirmacao"

    id_email_confirmacao = Column(Integer, primary_key=True, server_default=Identity(start=1))
    codigo = Column(String(6), nullable=False)
    id_usuario = Column(Integer, ForeignKey("usuario.id_usuario"), nullable=False)
