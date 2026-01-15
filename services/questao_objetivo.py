import re
import pandas as pd
from repository.objetivo import ObjetivoRepository
from repository.palavra import PalavraRepository
from repository.palavra_objetivo import PalavraObjetivoRepository
from repository.questao import QuestaoRepository
from repository.questao_objetivo import QuestaoObjetivoRepository


class QuestaoObjetivoService:
    def __init__(self, db):
        self.db = db

    def alinhar_questao_objetivo(self, id_questao: int, id_objetivo: int, qtd_palavras: int):
        questoes = QuestaoRepository.buscar_todas_questoes(self)
        df_questoes = pd.DataFrame(question.__dict__ for question in questoes)
        objetivos = ObjetivoRepository.buscar_todos_objetivos(self)
        df_objetivos = pd.DataFrame(obj.__dict__ for obj in objetivos)
        contador_match = 0

        for index, questao in df_questoes.iterrows():
            for jindex, objetivo in df_objetivos.iterrows():
                questao_objetivo = QuestaoObjetivoRepository.buscar_questao_objetivo(self, questao['id_questao'], objetivo['id_objetivo'])
                if questao_objetivo is not None:
                    continue
                else:
                    palavras_objetivo = PalavraObjetivoRepository.buscar_id_palavras_por_id_objetivo(self, objetivo['id_objetivo'])
                    for palavra_id in palavras_objetivo:
                        palavra = PalavraRepository.buscar_palavra_por_id(self, palavra_id)
                        if palavra and (re.search(r'\b' + re.escape(palavra.descricao_palavra) + r'\b', questao['resposta'], re.IGNORECASE) or re.search(r'\b' + re.escape(palavra.descricao_palavra) + r'\b', questao['descricao_questao'], re.IGNORECASE)):
                            contador_match += 1
                        # if palavra and (palavra.descricao_palavra in questao['resposta'] or palavra.descricao_palavra in questao['descricao_questao']):
                        #     contador_match += 1
                    QuestaoObjetivoRepository.inserir_questao_objetivo(self, questao['id_questao'], objetivo['id_objetivo'], contador_match)
            if contador_match > 0:
                contador_match = 0
        return True