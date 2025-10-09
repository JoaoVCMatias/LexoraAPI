from sqlalchemy import Column, Integer, Boolean, String, ForeignKey, DateTime
from database import Base
from sqlalchemy import Identity

class PalavreObjetivo(Base):
    __tablename__ = "palavra_objetivo"

    id_palavra_objetivo = Column(Integer, primary_key=True, server_default=Identity(start=1))
    id_palavra = Column(Integer, ForeignKey("palavra.id_palavra"), nullable=False)
    id_objetivo = Column(Integer, ForeignKey("objetivo.id_objetivo"), nullable=False)
