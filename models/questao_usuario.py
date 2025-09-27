from sqlalchemy import Column, Integer, Boolean, String, ForeignKey, DateTime
from database import Base
from sqlalchemy import Identity

class QuestaoUsuario(Base):
    __tablename__ = "questao_usuario"

    idquestaousuario = Column(Integer, primary_key=True, server_default=Identity(start=1))
    acerto = Column(Boolean)
    dataacerto = Column(String(3))
    idquestao = Column(Integer, ForeignKey("questao.idquestao"), nullable=False)
    idusuario = Column(Integer, ForeignKey("usuario.idusuario"), nullable=False)
    idconjuntoquestao = Column(Integer, ForeignKey("conjunto_questao.idconjuntoquestao"), nullable=False)
    datacriacao = Column(DateTime, nullable=False)
