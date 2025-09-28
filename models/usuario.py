from sqlalchemy import Column, Integer, String, Date, Boolean, ForeignKey, DateTime
from database import Base
from sqlalchemy import Identity

class Usuario(Base):
    __tablename__ = "usuario"

    id_usuario = Column(Integer, primary_key=True, server_default=Identity(start=1))
    nome = Column(String(150), nullable=False)
    data_nascimento = Column(Date, nullable=True)
    id_sexo = Column(Integer, ForeignKey("sexo.id_sexo"), nullable=True)
    email = Column(String(255), nullable=False)
    senha = Column(String(100), nullable=False)
    id_disponibilidade = Column(Integer, ForeignKey("disponibilidade.id_disponibilidade"), nullable=True)
    id_idiomamaterno = Column(Integer, ForeignKey("idioma.id_idioma"), nullable=True)
    cadastro_completo = Column(Boolean, nullable=False)
    ativo = Column(Boolean)
    data_ultimo_acesso = Column(DateTime, nullable=False)
    data_criacao = Column(DateTime, nullable=False)
    data_exclusao = Column(DateTime, nullable=True)
