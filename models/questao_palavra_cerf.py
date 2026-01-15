from sqlalchemy import Column, ForeignKey, Identity, Integer
from database import Base


class QuestaoPalavraCERF(Base):
    __tablename__ = "questao_palavra_CERF"

    id_questao_palavra_CERF = Column(Integer, primary_key=True, server_default=Identity(start=1))
    id_questao = Column(Integer, ForeignKey("questao.id_questao"), nullable=False)
    A1 = Column(Integer, nullable=False)
    A2 = Column(Integer, nullable=False)
    B1 = Column(Integer, nullable=False)
    B2 = Column(Integer, nullable=False)
    C1 = Column(Integer, nullable=False)
    C2 = Column(Integer, nullable=False)