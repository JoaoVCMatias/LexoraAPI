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

    def alinhar_questao_objetivo(self):
        questoes = QuestaoRepository.buscar_todas_questoes(self)
        df_questoes = pd.DataFrame(question.__dict__ for question in questoes)
        objetivos = ObjetivoRepository.buscar_todos_objetivos(self)
        df_objetivos = pd.DataFrame(obj.__dict__ for obj in objetivos)
        contador_match = 0
        query = ''
        i = 0
        tabela = [] # id_questao, id_objetivo, qtd_palavras

        for jindex, objetivo in df_objetivos.iterrows():
            palavras_objetivo = PalavraObjetivoRepository.buscar_id_palavras_por_id_objetivo(self, objetivo['id_objetivo'])
            for palavra_id in palavras_objetivo:
                palavra = PalavraRepository.buscar_palavra_por_id(self, palavra_id)
                questoes_search = df_questoes[df_questoes['resposta'].str.contains(r'\b' + re.escape(palavra.descricao_palavra) + r'\b', case=False, na=False) | df_questoes['descricao_questao'].str.contains(r'\b' + re.escape(palavra.descricao_palavra) + r'\b', case=False, na=False)]
                for index, questao in questoes_search.iterrows():
                    if any(d['id_questao'] == questao['id_questao'] and d['id_objetivo'] == objetivo['id_objetivo'] for d in tabela):
                        for d in tabela:
                            if d['id_questao'] == questao['id_questao'] and d['id_objetivo'] == objetivo['id_objetivo']:
                                d['qtd_palavras'] += 1
                    else:
                        tabela.append({
                            'id_questao': questao['id_questao'],
                            'id_objetivo': objetivo['id_objetivo'],
                            'qtd_palavras': 1
                        })

        for entry in tabela:
            questao_objetivo = QuestaoObjetivoRepository.buscar_questao_objetivo(self, entry['id_questao'], entry['id_objetivo'])
            if questao_objetivo is not None:
                continue
            else:
                query += QuestaoObjetivoRepository.inserir_questao_objetivo(self, entry['id_questao'], entry['id_objetivo'], entry['qtd_palavras'])
                query += "; "

        return query