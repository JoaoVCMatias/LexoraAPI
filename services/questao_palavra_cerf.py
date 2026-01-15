import re

import pandas as pd
from repository.palavra import PalavraRepository
from repository.questao import QuestaoRepository
from repository.questao_palavra_cerf import QuestaoPalavraCERFRepository


class QuestaoPalavraCERFService:
    def __init__(self, db):
        self.db = db

    def alinhar_questao_palavra_cefr(self):
        questoes = QuestaoRepository.buscar_todas_questoes(self)
        df_questoes = pd.DataFrame(question.__dict__ for question in questoes)
        palavras = PalavraRepository.buscar_todas_palavras(self)
        df_palavras = pd.DataFrame(palavra.__dict__ for palavra in palavras)
        contador_match = {}
        contador_match['A1'] = 0
        contador_match['A2'] = 0
        contador_match['B1'] = 0
        contador_match['B2'] = 0
        contador_match['C1'] = 0
        contador_match['C2'] = 0

        for index, questao in df_questoes.iterrows():
            verifica_existencia = QuestaoPalavraCERFRepository.buscar_questao_palavra_cerf(self, questao['id_questao'])
            if verifica_existencia is not None:
                continue
            else:
                for jindex, palavra in df_palavras.iterrows():
                    if (re.search(r'\b' + re.escape(palavra['descricao_palavra']) + r'\b', questao['resposta'], re.IGNORECASE) or re.search(r'\b' + re.escape(palavra['descricao_palavra']) + r'\b', questao['descricao_questao'], re.IGNORECASE)):
                        contador_match[palavra['CEFR']] += 1
                QuestaoPalavraCERFRepository.inserir_questao_palavra_cerf(self, questao['id_questao'], contador_match['A1'], contador_match['A2'], contador_match['B1'], contador_match['B2'], contador_match['C1'], contador_match['C2'])        
                contador_match['A1'] = 0
                contador_match['A2'] = 0
                contador_match['B1'] = 0
                contador_match['B2'] = 0
                contador_match['C1'] = 0
                contador_match['C2'] = 0