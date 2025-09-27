from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base
from sqlalchemy import Identity

class Questao(Base):
    __tablename__ = "questao"

    id_questao = Column(Integer, primary_key=True, server_default=Identity(start=1))
    json = Column(String(100), nullable=False)
    id_objetivo = Column(Integer, ForeignKey("objetivo.id_objetivo"), nullable=False)
    id_tipo_questao = Column(Integer, ForeignKey("tipo_questao.id_tipo_questao"), nullable=False)
    nivel = Column(Integer, nullable=False)
    caminho_arquivo = Column(String(100))
