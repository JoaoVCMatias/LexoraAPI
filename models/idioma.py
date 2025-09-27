from sqlalchemy import Column, Integer, String
from database import Base
from sqlalchemy import Identity

class Idioma(Base):
    __tablename__ = "idioma"

    ididioma = Column(Integer, primary_key=True, server_default=Identity(start=1))
    descricaoidioma = Column(String(50))
