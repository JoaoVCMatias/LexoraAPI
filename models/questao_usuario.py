from sqlalchemy import Column, Integer, Boolean, String, ForeignKey, DateTime
from database import Base
from sqlalchemy import Identity

class QuestaoUsuario(Base):
    __tablename__ = "questao_usuario"

    id_questao_usuario = Column(Integer, primary_key=True, server_default=Identity(start=1))
    acerto = Column(Boolean)
    resposta_usuario = Column(String(255), nullable=True)
    data_resposta = Column(DateTime)
    id_questao = Column(Integer, ForeignKey("questao.id_questao"), nullable=False)
    id_usuario = Column(Integer, ForeignKey("usuario.id_usuario"), nullable=False)
    id_conjunto_questao = Column(Integer, ForeignKey("conjunto_questao.id_conjunto_questao"), nullable=False)
    data_criacao = Column(DateTime, nullable=False)
