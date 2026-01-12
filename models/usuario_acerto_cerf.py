from sqlalchemy import Column, Integer, Boolean, String, ForeignKey, DateTime
from database import Base
from sqlalchemy import Identity

class Palavra(Base):
    __tablename__ = "usuario_acerto_cerf"

    id_usuario_acerto_cerf = Column(Integer, primary_key=True, server_default=Identity(start=1))
    id_usuario = Column(Integer, ForeignKey("usuario.id_usuario"), nullable=False)
    A1 = Column(Integer, nullable=False)
    A2 = Column(Integer, nullable=False)
    B1 = Column(Integer, nullable=False)
    B2 = Column(Integer, nullable=False)
    C1 = Column(Integer, nullable=False)
    C2 = Column(Integer, nullable=False)