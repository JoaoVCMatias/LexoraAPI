import random
import re
from fastapi import  HTTPException
from repository.conjunto_questao import ConjuntoQuestaoRepository
from repository.objetivo import ObjetivoRepository
from repository.objetivo_usuario import ObjetivoUsuarioRepository
from repository.palavra import PalavraRepository
from repository.palavra_objetivo import PalavraObjetivoRepository
from repository.questao import QuestaoRepository
from sqlalchemy.orm import Session
from datetime import date
from datetime import datetime
from repository.questao_objetivo import QuestaoObjetivoRepository
from repository.questao_usuario import QuestaoUsuarioRepository
from repository.usuario import UsuarioRepository
import json
import pandas as pd

class QuestaoService:

    def __init__(self, db: Session):
        self.db = db

    def buscar_questoes_usuario(self, id_usuario: int):
        i=0
        conjunto_questoes_ativa = ConjuntoQuestaoRepository.buscar_conjunto_questoes_ativas_usuario(self, id_usuario)
        if conjunto_questoes_ativa is not None and len(conjunto_questoes_ativa) > 0:
            id_conjunto_questao = conjunto_questoes_ativa[0].id_conjunto_questao
        else:
            id_conjunto_questao = ConjuntoQuestaoRepository.criar_conjunto_questao(self, id_usuario)

        questoes = QuestaoRepository.buscar_questoes_usuario(self, id_usuario, id_conjunto_questao)
        
        if questoes is not None:
            if len(questoes.questoes) < 10:
                while i < 10 - len(questoes.questoes):
                    id_questao = self.buscar_questao(id_usuario).get("id_questao")
                    if id_questao not in [q.id_questao for q in questoes.questoes]:
                        QuestaoUsuarioRepository.criar_questao_usuario(self, id_usuario, id_questao, id_conjunto_questao)
                        i += 1
                        questoes = QuestaoRepository.buscar_questoes_usuario(self, id_usuario, id_conjunto_questao)
        else:
            for i in range(10):
                id_questao = self.buscar_questao(id_usuario).get("id_questao")
                QuestaoUsuarioRepository.criar_questao_usuario(self, id_usuario, id_questao, id_conjunto_questao)
            questoes = QuestaoRepository.buscar_questoes_usuario(self, id_usuario, id_conjunto_questao)

        return questoes
        
    def buscar_questoes_usuario_old(self, id_usuario: int):
        return QuestaoRepository.buscar_questoes_usuario(self, id_usuario, None) 
    
    def buscar_questao(self, id_usuario: int):
        todas_questoes = QuestaoRepository.buscar_todas_questoes(self)
        df_questoes = pd.DataFrame(question.__dict__ for question in todas_questoes)
        usuario_objetivos = ObjetivoUsuarioRepository.pesquisar_objetivos_usuario(self, id_usuario)
        questoes_filtradas = pd.DataFrame()
        questao = None
        palavras_objetivos = []
        questao_objetivo = []
        df_questao_objetivo = pd.DataFrame()
        df_questoes_duplicadas = pd.DataFrame()

        # Buscar palavras relacionadas aos objetivos do usuário
        if usuario_objetivos is not None and len(usuario_objetivos) > 0:
            for obj in usuario_objetivos:
                questao_objetivo.extend(
                    QuestaoObjetivoRepository.buscar_questoes_por_objetivo(self, obj.id_objetivo)
                )
                palavras_objetivos.extend(
                    PalavraObjetivoRepository.buscar_id_palavras_por_id_objetivo(self, obj.id_objetivo)
                )

        # busca questoes que o usuario ja respondeu (memoria espaçada) usando a formula de fibonacci
        questoes_respondidas = QuestaoUsuarioRepository.buscar_questao_usuario_por_id_usuario(self, id_usuario) 
        df_questoes_respondidas = pd.DataFrame(questao_respondida.__dict__ for questao_respondida in questoes_respondidas)
        # df_questoes_respondidas = df_questoes_respondidas[['id_questao', 'data_resposta', 'acerto']]
        if questoes_respondidas is not None and len(questoes_respondidas) > 0:
            for index, row_questao_respondida in df_questoes_respondidas.iterrows():
                if row_questao_respondida['acerto'] is True:
                    id_questao = row_questao_respondida['id_questao']
                    data_resposta = row_questao_respondida['data_resposta']
                    dias_desde_resposta = (date.today() - pd.to_datetime(data_resposta).date()).days
                    # Sequência de Fibonacci para espaçamento                    

        # busca quuestoes que possuem mais de um objetivo relacionado ao usuario
        df_questao_objetivo = pd.DataFrame(questao_objetivo.__dict__ for questao_objetivo in questao_objetivo)
        ids = df_questao_objetivo['id_questao'].tolist() if not df_questao_objetivo.empty else []
        if ids:
            df_questoes_duplicadas = df_questoes[df_questoes['id_questao'].isin(ids)].drop_duplicates(subset=['id_questao'])
        if not df_questoes_duplicadas.empty:
            df_questoes = df_questoes_duplicadas

        # Filtrar questões que contenham as palavras relacionadas aos objetivos
        if palavras_objetivos is not None and len(palavras_objetivos) > 0:
            i = 0
            random.shuffle(palavras_objetivos)
            while questao is None and i < len(palavras_objetivos):
                palavra = PalavraRepository.buscar_palavra_por_id(self, str(palavras_objetivos[i]))
                if palavra is not None:
                    questoes_filtradas = df_questoes[df_questoes['resposta'].str.contains('\\b'+palavra.descricao_palavra+'\\b', case=False, na=False)]
                    if not questoes_filtradas.empty:
                        questao = questoes_filtradas[questoes_filtradas['resposta'].str.contains('\\b'+palavra.descricao_palavra+'\\b', case=False, na=False)].sample(frac=1).to_dict(orient='records')[0]
                    else:
                        questoes_filtradas = df_questoes[df_questoes['descricao_questao'].str.contains('\\b'+palavra.descricao_palavra+'\\b', case=False, na=False)]
                        if not questoes_filtradas.empty:
                            questao = questoes_filtradas[questoes_filtradas['descricao_questao'].str.contains('\\b'+palavra.descricao_palavra+'\\b', case=False, na=False)].sample(frac=1).to_dict(orient='records')[0]
                i += 1
            if questao is None:
                questao = df_questoes.sample(frac=1).to_dict(orient='records')[0]

        return questao

    def gerar_questao_id(self, id_usuario: int):
        # id_objetivo_usuario = ObjetivoUsuarioRepository.pesquisar_objetivo_usuario(self, id_usuario)
        # id_objetivos = [obj.id_objetivo for obj in id_objetivo_usuario]
        # if not id_objetivos:
        #     raise HTTPException(status_code=400, detail="Usuário não possui objetivos cadastrados.")
        
        # questoes_usuario = self.buscar_questoes_usuario(id_usuario)
        # if questoes_usuario is not None and len(questoes_usuario.questoes) > 0:
        #     return questoes_usuario
        
        # date_atual = datetime.now()
        # ids_questao = QuestaoRepository.buscar_questoes(self, id_usuario, 5, 2)
        # id_conjunto = QuestaoRepository.inserir_conjunto_questoes(self, id_usuario, date_atual)

        # QuestaoRepository.inserir_questao_usuario(self, id_usuario, ids_questao, id_conjunto, date_atual) 
        # return self.buscar_questoes_usuario(id_usuario)
        return self.buscar_questao(id_usuario)

    def gerar_questao_id_old(self, id_usuario: int):
        questoes_usuario = self.buscar_questoes_usuario_old(id_usuario)
        if questoes_usuario is not None and len(questoes_usuario.questoes) > 0:
             return questoes_usuario
        
        date_atual = datetime.now()
        ids_questao = QuestaoRepository.buscar_questoes(self, id_usuario, 5, 2)
        id_conjunto = QuestaoRepository.inserir_conjunto_questoes(self, id_usuario, date_atual)
        QuestaoRepository.inserir_questao_usuario(self, id_usuario, ids_questao, id_conjunto, date_atual) 
        return self.buscar_questoes_usuario_old(id_usuario)


    def responder_questao(self, id_usuario: int, id_questao: int, alternariva: int, id_conjunto_questao: int):
        usuario = UsuarioRepository.buscar_usuario_por_id(self, id_usuario)
        if not usuario:
            return HTTPException(status_code=404, detail="Usuário não encontrado.")
        
        questoes_usuario = QuestaoRepository.buscar_questoes_usuario(self, id_usuario, None).questoes
        conclusao = sum(1 for questao in questoes_usuario if questao.acerto is None) == 1 

        questao = QuestaoRepository.buscar_questao_por_id(self, id_questao)
        if not questao:
            raise HTTPException(status_code=404, detail="Questão não encontrada.")
        
        correta = True

        alterenativas_questao = json.loads(questao.json_opcao)
        print(alterenativas_questao)
        if alterenativas_questao[alternariva] is None:
            raise HTTPException(status_code=400, detail="Alternativa inválida.")
        elif alterenativas_questao[alternariva] != questao.resposta:
            correta = False
        
        data_resposta = datetime.now()

        QuestaoRepository.responder_questao(self, id_usuario, id_questao, correta, alterenativas_questao[alternariva], id_conjunto_questao, data_resposta)
        if conclusao:
            QuestaoRepository.concluir_conjunto_questoes(self, id_conjunto_questao, data_resposta)

        return correta 
    
    def gerar_relatorio_questoes_usuario(self, id_usuario: int):
        relatorio = QuestaoRepository.relatorio_desenpenho_usuario(self, id_usuario)
        for r in relatorio:
            questoes = QuestaoRepository.buscar_questoes_usuario(self, id_usuario, r.id_conjunto_questao)
            r.questoes.append(questoes) 
        return relatorio

    