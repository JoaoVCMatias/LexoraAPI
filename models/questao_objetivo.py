from sqlalchemy import Column, Integer, Boolean, String, ForeignKey, DateTime
from database import Base
from sqlalchemy import Identity

class QuestaoObjetivo(Base):
    __tablename__ = "questao_objetivo"

    id_questao_objetivo = Column(Integer, primary_key=True, server_default=Identity(start=1))
    id_questao = Column(Integer, ForeignKey("questao.id_questao"), nullable=False)
    id_objetivo = Column(Integer, ForeignKey("objetivo.id_objetivo"), nullable=False)
    qtq_palavras = Column(Integer, nullable=False)