from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base
from sqlalchemy import Identity

class Questao(Base):
    __tablename__ = "questao"

    id_questao = Column(Integer, primary_key=True, server_default=Identity(start=1))
    descricao_questao = Column(String(100), nullable=False)
    json_opcao = Column(String(100), nullable=True)
    resposta = Column(String(50), nullable=True)
    id_tipo_questao = Column(Integer, ForeignKey("tipo_questao.id_tipo_questao"), nullable=False)
    nivel = Column(Integer, nullable=False)
    caminho_arquivo = Column(String(100))
