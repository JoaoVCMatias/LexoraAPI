import datetime
from requests import Session
from repository.conjunto_questao import ConjuntoQuestaoRepository
from repository.questao import QuestaoRepository
from repository.questao_usuario import QuestaoUsuarioRepository
from schemas.usuario import RelatorioDesempenhoUsuarioResponse
from services.questao import QuestaoService


class ConjuntoQuestoesService:

    def __init__(self, db: Session):
        self.db = db

    def criar_conjunto_questao(self, id_usuario: int):
        conjunto_questao = ConjuntoQuestaoRepository(self.db)
        id_conjunto_questao = conjunto_questao.criar_conjunto_questao(id_usuario)
        return id_conjunto_questao

    def resultado_conjunto_questao(self, id_usuario: int, id_conjunto_questao: int):
        resultado =  QuestaoRepository.resultado_conjunto_questoes(self, id_usuario, id_conjunto_questao)
        for r in resultado:
            questoes = QuestaoRepository.buscar_questoes_usuario(self, id_usuario, id_conjunto_questao)
            r.questoes.append(questoes)
            
        return resultado