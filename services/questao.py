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
from repository.questao_palavra_cerf import QuestaoPalavraCERFRepository
from repository.questao_usuario import QuestaoUsuarioRepository
from repository.usuario import UsuarioRepository
import json
import pandas as pd

from repository.usuario_acerto_cerf import UsuarioAcertoCERFRepository

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
                while i < (10 - len(questoes.questoes)):
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
    
    def buscar_questao(self, id_usuario: int, id_conjunto_questao: int = None):
        todas_questoes = QuestaoRepository.buscar_todas_questoes(self)
        df_questoes = pd.DataFrame(question.__dict__ for question in todas_questoes)
        usuario_objetivos = ObjetivoUsuarioRepository.pesquisar_objetivos_usuario(self, id_usuario)
        questoes_filtradas = pd.DataFrame()
        questao = None
        palavras_objetivos = []
        questao_objetivo = []
        conjunto_questao = [] 
        df_conjunto_questao = pd.DataFrame()  
        df_questao_objetivo = pd.DataFrame()
        df_questoes_duplicadas = pd.DataFrame()

        if id_conjunto_questao is not None:
            conjunto_ativo = ConjuntoQuestaoRepository.buscar_conjunto_questoes_ativas_usuario(self, id_usuario)
            if conjunto_ativo is not None and len(conjunto_ativo) > 0:
                id_conjunto_questao = conjunto_ativo[0].id_conjunto_questao
            conjunto_questao = QuestaoRepository.buscar_questoes_usuario(self, id_usuario, id_conjunto_questao).questoes
            df_conjunto_questao = pd.DataFrame(questao_conjunto.__dict__ for questao_conjunto in conjunto_questao)
            df_questoes = df_questoes[~df_questoes['id_questao'].isin(df_conjunto_questao['id_questao'].tolist())]

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
        questoes_respondidas = QuestaoUsuarioRepository.buscar_questoes_usuario_respondidas_por_id_usuario(self, id_usuario) 
        df_questoes_respondidas = pd.DataFrame(questao_respondida.__dict__ for questao_respondida in questoes_respondidas)
        # df_questoes_respondidas = df_questoes_respondidas[['id_questao', 'data_resposta', 'acerto']]
        if questoes_respondidas is not None and len(questoes_respondidas) > 0:
            for index, row_questao_respondida in df_questoes_respondidas.iterrows():
                historico_questao = df_questoes_respondidas[df_questoes_respondidas['id_questao'] == row_questao_respondida['id_questao']]
                historico_questao = historico_questao.sort_values(by='data_resposta', ascending=False)
                contador_acertos = 0
                ultimo = historico_questao.iloc[-1]
                for i in range(len(historico_questao)):
                    if historico_questao.iloc[i]['acerto'] is True and (date.today() - pd.to_datetime(data_resposta).date()).days >= 0:
                        contador_acertos += 1
                    else:
                        break

                if contador_acertos > 0:
                    data_ultima_resposta = pd.to_datetime(ultimo['data_resposta']).date()
                    qtd_dias_repetir = ((1+5**(1/2))**contador_acertos -(1+5**(1/2))**contador_acertos)/(2**contador_acertos)*(1+5**(1/2)) # Sequência de Fibonacci simplificada
                    if data_ultima_resposta + pd.Timedelta(days=qtd_dias_repetir) >= pd.to_datetime(date.today()).date():
                        print(qtd_dias_repetir)
                        print("data ultima resposta:", data_ultima_resposta)
                        print("REPETE HOJEEEEEEEEEEEE")
                
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
        a1, a2, b1, b2, c1, c2 = 0, 0, 0, 0, 0, 0
        if not usuario:
            return HTTPException(status_code=404, detail="Usuário não encontrado.")
        
        questoes_usuario = QuestaoRepository.buscar_questoes_usuario(self, id_usuario, id_conjunto_questao).questoes
        questoes_respondidas = [questao for questao in questoes_usuario if questao.resposta_usuario is not None]
        conclusao = True if len(questoes_respondidas) == len(questoes_usuario) else False

        questao = QuestaoRepository.buscar_questao_por_id(self, id_questao)
        if not questao:
            raise HTTPException(status_code=404, detail="Questão não encontrada.")
        
        correta = True

        alterenativas_questao = json.loads(questao.json_opcao)
        if alterenativas_questao[alternariva] is None:
            raise HTTPException(status_code=400, detail="Alternativa inválida.")
        elif alterenativas_questao[alternariva] != questao.resposta:
            correta = False
        
        data_resposta = datetime.now()

        questao_palavra_cerf = QuestaoPalavraCERFRepository.buscar_questao_palavra_cerf_por_id_questao(self, id_questao)
        if questao_palavra_cerf is not None:
            if questao_palavra_cerf.A1 > 0:
                a1 = 1 if correta else 0
            if questao_palavra_cerf.A2 > 0:
                a2 = 1 if correta else 0
            if questao_palavra_cerf.B1 > 0:
                b1 = 1 if correta else 0
            if questao_palavra_cerf.B2 > 0:
                b2 = 1 if correta else 0
            if questao_palavra_cerf.C1 > 0:
                c1 = 1 if correta else 0
            if questao_palavra_cerf.C2 > 0:
                c2 = 1 if correta else 0
        print("A1:", a1, "A2:", a2, "B1:", b1, "B2:", b2, "C1:", c1, "C2:", c2)

        usuario_acerto_cerf = UsuarioAcertoCERFRepository.buscar_acertos_cerf_por_id_usuario(self, id_usuario)
        if usuario_acerto_cerf is None:
            usuario_acerto_cerf = UsuarioAcertoCERFRepository.add_usuario_acerto_cerf(self, id_usuario, a1, a2, b1, b2, c1, c2)
        else:
            if correta:
                a1_total = usuario_acerto_cerf.A1 + a1
                a2_total = usuario_acerto_cerf.A2 + a2
                b1_total = usuario_acerto_cerf.B1 + b1
                b2_total = usuario_acerto_cerf.B2 + b2
                c1_total = usuario_acerto_cerf.C1 + c1
                c2_total = usuario_acerto_cerf.C2 + c2
                print("TOTAL ACERTOU - A1:", a1_total, "A2:", a2_total, "B1:", b1_total, "B2:", b2_total, "C1:", c1_total, "C2:", c2_total)
            else:
                a1_total = max(0, (usuario_acerto_cerf.A1-1))
                a2_total = max(0, (usuario_acerto_cerf.A2-1))
                b1_total = max(0, (usuario_acerto_cerf.B1-1))
                b2_total = max(0, (usuario_acerto_cerf.B2-1))
                c1_total = max(0, (usuario_acerto_cerf.C1-1))
                c2_total = max(0, (usuario_acerto_cerf.C2-1))
                print("TOTAL ERROU - A1:", a1_total, "A2:", a2_total, "B1:", b1_total, "B2:", b2_total, "C1:", c1_total, "C2:", c2_total)
            UsuarioAcertoCERFRepository.update_usuario_acerto_cerf(self, id_usuario, a1_total, a2_total, b1_total, b2_total, c1_total, c2_total)

        QuestaoRepository.responder_questao(self, id_usuario, id_questao, correta, alterenativas_questao[alternariva], id_conjunto_questao, data_resposta)
        if conclusao:
            ConjuntoQuestaoRepository.concluir_conjunto_questao(self, id_usuario, id_conjunto_questao, data_resposta)
            
        return correta 
    
    def gerar_relatorio_questoes_usuario(self, id_usuario: int):
        relatorio = QuestaoRepository.relatorio_desenpenho_usuario(self, id_usuario)
        for r in relatorio:
            questoes = QuestaoRepository.buscar_questoes_usuario(self, id_usuario, r.id_conjunto_questao)
            r.questoes.append(questoes) 
        return relatorio

    