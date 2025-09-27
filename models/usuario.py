from sqlalchemy import Column, Integer, String, Date, Boolean, ForeignKey, DateTime
from database import Base
from sqlalchemy import Identity

class Usuario(Base):
    __tablename__ = "usuario"

    idusuario = Column(Integer, primary_key=True, server_default=Identity(start=1))
    nome = Column(String(150), nullable=False)
    datanascimento = Column(Date, nullable=False)
    idsexo = Column(Integer, ForeignKey("sexo.idsexo"), nullable=False)
    email = Column(String(255), nullable=False)
    senha = Column(String(100), nullable=False)
    iddisponibilidade = Column(Integer, ForeignKey("disponibilidade.iddisponibilidade"), nullable=False)
    ididiomamaterno = Column(Integer, ForeignKey("idioma.ididioma"), nullable=False)
    cadastrocompleto = Column(Boolean, nullable=False)
    ativo = Column(Boolean)
    dataultimoacesso = Column(DateTime, nullable=False)
    datacriacao = Column(DateTime, nullable=False)
    dataexclusao = Column(DateTime, nullable=False)
