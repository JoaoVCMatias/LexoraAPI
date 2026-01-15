<<<<<<< HEAD
from sqlalchemy import Column, ForeignKey, Identity, Integer
from database import Base


class UsuarioAcertoCERF(Base):
    __tablename__ = "usuario_acerto_CERF"

    id_usuario_acerto_CERF = Column(Integer, primary_key=True, server_default=Identity(start=1))
=======
from sqlalchemy import Column, Integer, Boolean, String, ForeignKey, DateTime
from database import Base
from sqlalchemy import Identity

class UsuarioAcertoCerf(Base):
    __tablename__ = "usuario_acerto_cerf"

    id_usuario_acerto_cerf = Column(Integer, primary_key=True, server_default=Identity(start=1))
>>>>>>> 830f987cd9df97cfea7f4b4afad0764cbe295017
    id_usuario = Column(Integer, ForeignKey("usuario.id_usuario"), nullable=False)
    A1 = Column(Integer, nullable=False)
    A2 = Column(Integer, nullable=False)
    B1 = Column(Integer, nullable=False)
    B2 = Column(Integer, nullable=False)
    C1 = Column(Integer, nullable=False)
<<<<<<< HEAD
    C2 = Column(Integer, nullable=False)
    
=======
    C2 = Column(Integer, nullable=False)
>>>>>>> 830f987cd9df97cfea7f4b4afad0764cbe295017
