import datetime
from requests import Session
from repository.conjunto_questao import ConjuntoQuestaoRepository


class ConjuntoQuestoesService:

    def __init__(self, db: Session):
        self.db = db

    def criar_conjunto_questao(self, id_usuario: int):
        conjunto_questao = ConjuntoQuestaoRepository(self.db)
        id_conjunto_questao = conjunto_questao.criar_conjunto_questao(id_usuario)
        return id_conjunto_questao