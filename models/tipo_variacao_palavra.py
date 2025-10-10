from sqlalchemy import Column, Integer, String
from database import Base
from sqlalchemy import Identity

class TipoVariacaoPalavra(Base):
    __tablename__ = "tipo_variacao_palavra"

    id_tipo_variacao_palavra = Column(Integer, primary_key=True, server_default=Identity(start=1))
    descricao_tipo_variacao_palavra = Column(String(45), nullable=False)
