from sqlalchemy import Column, Integer, String
from database import Base
from sqlalchemy import Identity

class TipoQuestao(Base):
    __tablename__ = "tipo_questao"

    id_tipo_questao = Column(Integer, primary_key=True, server_default=Identity(start=1))
    descricao_tipo_questao = Column(String(50), nullable=False)
