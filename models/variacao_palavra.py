from sqlalchemy import Column, Integer, Text, ForeignKey
from database import Base
from sqlalchemy import Identity

class VariacaoPalavra(Base):
    __tablename__ = "variacao_palavra"

    id_variacao_palavra = Column(Integer, primary_key=True, server_default=Identity(start=1))
    id_palavra = Column(Integer, ForeignKey("palavra.id_palavra"), nullable=False)
    id_tipo_variacao_palavra = Column(Integer, ForeignKey("tipo_variacao_palavra.id_tipo_variacao_palavra"), nullable=False)
    id_palavra_variacao = Column(Integer, ForeignKey("palavra.id_palavra"), nullable=False)
