from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base
from sqlalchemy import Identity

class EmailConfirmacao(Base):
    __tablename__ = "email_confirmacao"

    idemailconfirmacao = Column(Integer, primary_key=True, server_default=Identity(start=1))
    codigo = Column(String(6), nullable=False)
    idusuario = Column(Integer, ForeignKey("usuario.idusuario"), nullable=False)
