<<<<<<< HEAD
from sqlalchemy import Column, ForeignKey, Identity, Integer
from database import Base


class QuestaoPalavraCERF(Base):
    __tablename__ = "questao_palavra_CERF"

    id_questao_palavra_CERF = Column(Integer, primary_key=True, server_default=Identity(start=1))
=======
from sqlalchemy import Column, Integer, Boolean, String, ForeignKey, DateTime
from database import Base
from sqlalchemy import Identity

class QuestaoPalavraCerf(Base):
    __tablename__ = "questao_palavra_cerf"

    id_questao_palavra_cerf = Column(Integer, primary_key=True, server_default=Identity(start=1))
>>>>>>> 830f987cd9df97cfea7f4b4afad0764cbe295017
    id_questao = Column(Integer, ForeignKey("questao.id_questao"), nullable=False)
    A1 = Column(Integer, nullable=False)
    A2 = Column(Integer, nullable=False)
    B1 = Column(Integer, nullable=False)
    B2 = Column(Integer, nullable=False)
    C1 = Column(Integer, nullable=False)
    C2 = Column(Integer, nullable=False)