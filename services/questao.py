import random
import re
from fastapi import  HTTPException
from config import TZ_BRASIL
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
from repository.relatorio import RelatorioRepository
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
        meta = RelatorioRepository.buscar_metas_usuario(self, id_usuario)
        print(meta.meta)
        
        if questoes is not None:
            if len(questoes.questoes) < meta.meta:
                while i < (meta.meta - len(questoes.questoes)):
                    id_questao = self.buscar_questao(id_usuario).get("id_questao")
                    if id_questao not in [q.id_questao for q in questoes.questoes]:
                        QuestaoUsuarioRepository.criar_questao_usuario(self, id_usuario, id_questao, id_conjunto_questao)
                        i += 1
                        questoes = QuestaoRepository.buscar_questoes_usuario(self, id_usuario, id_conjunto_questao)
        else:
            while i < meta.meta:
                id_questao = self.buscar_questao(id_usuario).get("id_questao")
                QuestaoUsuarioRepository.criar_questao_usuario(self, id_usuario, id_questao, id_conjunto_questao)
                i = i + 1
            questoes = QuestaoRepository.buscar_questoes_usuario(self, id_usuario, id_conjunto_questao)
        
        return questoes
        
    def buscar_questoes_usuario_old(self, id_usuario: int):
        return QuestaoRepository.buscar_questoes_usuario(self, id_usuario, None) 
    
    def buscar_questao(self, id_usuario: int, id_conjunto_questao: int = None):
        questao_usuario_cadastra = self.buscar_questoes_usuario_old(id_usuario)
        if questao_usuario_cadastra is not None and len(questao_usuario_cadastra.questoes) > 0:
            return questao_usuario_cadastra
        
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
        fibonacci_sequence = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
        tabela_retencao = self.calcula_taxa_esquecimento(id_usuario)

        if id_conjunto_questao is None:
            conjunto_ativo = ConjuntoQuestaoRepository.buscar_conjunto_questoes_ativas_usuario(self, id_usuario)
            if conjunto_ativo is not None and len(conjunto_ativo) > 0:
                id_conjunto_questao = conjunto_ativo[0].id_conjunto_questao
            else:
                id_conjunto_questao = ConjuntoQuestaoRepository.criar_conjunto_questao(self, id_usuario)

        if id_conjunto_questao is None:      
            conjunto_ativo = ConjuntoQuestaoRepository.buscar_conjunto_questoes_ativas_usuario(self, id_usuario)
            id_conjunto_questao = conjunto_ativo[0].id_conjunto_questao

        conjunto_questao = QuestaoRepository.buscar_questoes_usuario(self, id_usuario, id_conjunto_questao)
        print(conjunto_questao)
        
        if conjunto_questao:
            conjunto_questao = conjunto_questao.questoes
        if conjunto_questao:
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

        # busca questoes que o usuario ja respondeu para revisão (memoria espaçada) usando a formula de fibonacci
        questoes_respondidas = QuestaoUsuarioRepository.buscar_questoes_usuario_respondidas_por_id_usuario(self, id_usuario) 
        
        if questoes_respondidas is not None and len(questoes_respondidas) > 0:
            df_questoes_respondidas = pd.DataFrame(questao_respondida.__dict__ for questao_respondida in questoes_respondidas)
            df_questoes_respondidas = df_questoes_respondidas[['id_questao', 'data_resposta', 'acerto']]
            df_questoes_respondidas = df_questoes_respondidas[~df_questoes_respondidas['id_questao'].isin(df_conjunto_questao['id_questao'].tolist())]
            
            for index, row_questao_respondida in df_questoes_respondidas.iterrows():
                df_historico_questao = self.calcula_tempo_resposta_historico_questao(id_usuario, row_questao_respondida['id_questao'])
                if df_historico_questao is not None and not df_historico_questao.empty:
                    # df_historico_questao = pd.DataFrame(historico.__dict__ for historico in historico_questao)     
                    dias_desde_ultima_resposta = (date.today() - row_questao_respondida['data_resposta'].date()).days
                    taxa_esquecimento = 0
                    if not tabela_retencao[tabela_retencao['dias_entre_questoes'] == dias_desde_ultima_resposta].empty:
                        if tabela_retencao[tabela_retencao[dias_desde_ultima_resposta]]['data_resposta'] > 0:
                            taxa_esquecimento = 1 - tabela_retencao[tabela_retencao[dias_desde_ultima_resposta]]['taxa_acerto']
                    tentativas = len(df_historico_questao)
                    if tentativas-1 < len(fibonacci_sequence) and taxa_esquecimento > 0:
                        intervalo_fibonacci = fibonacci_sequence[tentativas-1]
                        if dias_desde_ultima_resposta >= intervalo_fibonacci:
                            questoes_filtradas = pd.concat([questoes_filtradas, df_questoes[df_questoes['id_questao'] == row_questao_respondida['id_questao']]])          

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
                    df_questoes_filtradas = df_questoes[df_questoes['resposta'].str.contains('\\b'+palavra.descricao_palavra+'\\b', case=False, na=False)]
                    if not df_questoes_filtradas.empty:
                        questoes_filtradas = pd.concat([questoes_filtradas, df_questoes_filtradas])
                    
                    df_questoes_filtradas = df_questoes[df_questoes['resposta'].str.contains('\\b'+palavra.descricao_palavra+'\\b', case=False, na=False)]
                    if not df_questoes_filtradas.empty:
                        questoes_filtradas = pd.concat([questoes_filtradas, df_questoes_filtradas])
                i += 1
            if not questoes_filtradas.empty and len(questoes_filtradas) > 0:
                questao = questoes_filtradas.sample(frac=1).to_dict(orient='records')[0]
            else:
                questoes_filtradas = df_questoes[df_questoes['descricao_questao'].str.contains('\\b'+palavra.descricao_palavra+'\\b', case=False, na=False)]
                if not questoes_filtradas.empty:
                    questao = questoes_filtradas[questoes_filtradas['descricao_questao'].str.contains('\\b'+palavra.descricao_palavra+'\\b', case=False, na=False)].sample(frac=1).to_dict(orient='records')[0]
                    
            if questao is None:
                questao = df_questoes.sample(frac=1).to_dict(orient='records')[0]

        # self.busca_palavras_traducao(questao)
        # print(questao['id_questao'])
        # print(self.calcula_tempo_resposta_historico_questao(id_usuario, 37))
        # print(self.calcula_tempo_resposta_conjunto(id_usuario, 37, 3))

        return questao

    def busca_palavras_traducao(self, questao: dict):
        palavras_descricao = questao['descricao_questao'].split()
        opcoes_questao = json.loads(questao['json_opcao'])
        print(questao['descricao_questao'])
        i = 0

        print('######### questao #############')
        for palavra_desc in palavras_descricao:
            palavra_desc = re.sub(r'_', '', palavra_desc)  # Remove underlines
            palavra_traduzida = PalavraRepository.busca_palavra_por_descricao(self, palavra_desc)

            if palavra_traduzida:
                df_palavra_traduzida = pd.DataFrame(palavra_t.__dict__ for palavra_t in palavra_traduzida)
                df_palavra_traduzida = df_palavra_traduzida[['descricao_palavra', 'descricao_palavra_traducao']]
                df_palavra_traduzida = df_palavra_traduzida.drop_duplicates()
                for index, traducao in df_palavra_traduzida.iterrows():
                    if traducao['descricao_palavra_traducao']:
                        print(i)
                        print(palavra_desc)
                        print(traducao['descricao_palavra_traducao'])
                        print('######')
            i = i + 1

        i = 0
        print("######### OPÇÕES #########")
        for opc in opcoes_questao:
            palavra_traduzida = PalavraRepository.busca_palavra_por_descricao(self, opc)

            if palavra_traduzida:
                df_palavra_traduzida = pd.DataFrame(palavra_t.__dict__ for palavra_t in palavra_traduzida)
                df_palavra_traduzida = df_palavra_traduzida[['descricao_palavra', 'descricao_palavra_traducao']]
                df_palavra_traduzida = df_palavra_traduzida.drop_duplicates()
                for index, traducao in df_palavra_traduzida.iterrows():
                    if traducao['descricao_palavra_traducao']:
                        print(i)
                        print(opc)
                        print(traducao['descricao_palavra_traducao'])
                        print('#########')   
            i = i + 1


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
        
        date_atual = datetime.now(TZ_BRASIL)
        ids_questao = QuestaoRepository.buscar_questoes(self, id_usuario, 5, 2)
        id_conjunto = QuestaoRepository.inserir_conjunto_questoes(self, id_usuario, date_atual)
        QuestaoRepository.inserir_questao_usuario(self, id_usuario, ids_questao, id_conjunto, date_atual) 
        return self.buscar_questoes_usuario_old(id_usuario)


    def responder_questao(self, id_usuario: int, id_questao: int, alternariva: int, id_conjunto_questao: int):
        usuario = UsuarioRepository.buscar_usuario_por_id(self, id_usuario)
        a1, a2, b1, b2, c1, c2 = 0, 0, 0, 0, 0, 0
        if not usuario:
            return HTTPException(status_code=404, detail="Usuário não encontrado.")

        questao = QuestaoRepository.buscar_questao_por_id(self, id_questao)
        if not questao:
            raise HTTPException(status_code=404, detail="Questão não encontrada.")
        
        correta = True

        alterenativas_questao = json.loads(questao.json_opcao)
        if alterenativas_questao[alternariva] is None:
            raise HTTPException(status_code=400, detail="Alternativa inválida.")
        elif alterenativas_questao[alternariva] != questao.resposta:
            correta = False

        data_resposta = datetime.now(TZ_BRASIL)

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

        questoes_usuario = QuestaoRepository.buscar_questoes_usuario(self, id_usuario, id_conjunto_questao).questoes
        questoes_respondidas = [questao for questao in questoes_usuario if questao.resposta_usuario is not None]
        conclusao = True if len(questoes_respondidas) == len(questoes_usuario) else False

        if conclusao:
            ConjuntoQuestaoRepository.concluir_conjunto_questao(self, id_usuario, id_conjunto_questao, data_resposta)
            
        return correta 
    
    def gerar_relatorio_questoes_usuario(self, id_usuario: int):
        relatorio = QuestaoRepository.relatorio_desenpenho_usuario(self, id_usuario)
        if relatorio is None:
            return None
        for r in relatorio:
            questoes = QuestaoRepository.buscar_questoes_usuario(self, id_usuario, r.id_conjunto_questao)
            r.questoes.append(questoes) 
        return relatorio

    def buscar_questoes_usuario_por_conjunto(self, id_usuario: int, id_conjunto_questao: int | None = None):
        questoes = QuestaoRepository.buscar_questoes_usuario(self, id_usuario, id_conjunto_questao)
        return questoes

    def calcula_dificuldade_questao(self, id_questao: int):
        dificuldade = 0
        questao_cerf = QuestaoPalavraCERFRepository.buscar_questao_palavra_cerf_por_id_questao(self, id_questao)

        if questao_cerf:
            soma = (1 * questao_cerf.A1) + ( 2 * questao_cerf.A2) + (3 * questao_cerf.B1) + (4 * questao_cerf.B2) + (5 * questao_cerf.C1) + (6 * questao_cerf.C2)
            dificuldade = soma / 6

        return dificuldade

    def calcula_desempenho_conjunto(self, id_conjunto: int):
        conjunto = QuestaoUsuarioRepository.buscar_questoes_por_conjunto_id(self, id_conjunto)
        total_questoes = len(conjunto)
        acertos = sum(1 for q in conjunto if q.acerto)
        desempenho = (acertos / total_questoes) if total_questoes > 0 else 0

        return desempenho
    
    def calcula_desempenho_questao_usuario(self, id_usuario: int, id_questao: int):
        questoes_usuario = QuestaoUsuarioRepository.buscar_questoes_usuario_por_id_questao(self, id_usuario, id_questao)
        desempenho = 0

        if questoes_usuario:
            df_questoes_usuario = pd.DataFrame(questao_usuario.__dict__ for questao_usuario in questoes_usuario)
            df_questoes_usuario = df_questoes_usuario.sort_values(by="data_resposta")
            total_respondidas = len(df_questoes_usuario)
            total_acertos = df_questoes_usuario['acerto'].sum()
            desempenho = (total_acertos / total_respondidas) if total_respondidas > 0 else 0

        return desempenho
    
    def calcula_tempo_resposta_conjunto(self, id_usuario: int, id_questao: int, id_conjunto: int):
        conjunto = ConjuntoQuestaoRepository.buscar_conjunto_questao_por_id(self, id_conjunto)
        questoes_conjunto = QuestaoUsuarioRepository.buscar_questoes_por_conjunto_id(self, id_conjunto)

        if questoes_conjunto:
            df_questoes_conjunto = pd.DataFrame(questao_conjunto.__dict__ for questao_conjunto in questoes_conjunto) 
            df_questoes_conjunto = df_questoes_conjunto.sort_values(by="data_resposta")
            lista_tempo_resposta = []

            for index, row in df_questoes_conjunto.iterrows():
                if index == 0:
                    lista_tempo_resposta.append(
                        (row['data_resposta'] - conjunto.data_criacao).total_seconds()
                    )
                else:
                    lista_tempo_resposta.append(
                        (row['data_resposta'] - df_questoes_conjunto.iloc[index - 1]['data_resposta']).total_seconds()
                    )
            
            df_questoes_conjunto['tempo_resposta'] = lista_tempo_resposta
            
            return df_questoes_conjunto
        else:
            return None
    
    def calcula_tempo_resposta_historico_questao(self, id_usuario: int, id_questao: int):
        historico = QuestaoUsuarioRepository.buscar_questoes_respondidas_usuario_por_id_questao(self, id_usuario, id_questao)

        if historico:
            df_historico = pd.DataFrame(h.__dict__ for h in historico)
            lista_tempo_resposta = []

            for index, hist in df_historico.iterrows():
                if hist['id_conjunto_questao'] is None:
                    df_historico = df_historico.drop(index)
                else:
                    conjunto = ConjuntoQuestaoRepository.buscar_conjunto_questao_por_id(self, hist['id_conjunto_questao'])
                    questoes_conjunto = QuestaoUsuarioRepository.buscar_questoes_por_conjunto_id(self, hist['id_conjunto_questao'])
                    df_questoes_conjunto = pd.DataFrame(questao_conjunto.__dict__ for questao_conjunto in questoes_conjunto)
                    df_questoes_conjunto = df_questoes_conjunto.sort_values(by="data_resposta")
                    index_questao = df_questoes_conjunto[df_questoes_conjunto['id_questao']==id_questao].index
                    if index_questao == 0:
                        lista_tempo_resposta.append(
                            (hist['data_resposta'] - conjunto.data_criacao).total_seconds()
                        )
                    else:
                        # print(hist['data_resposta'])
                        # print(df_questoes_conjunto.iloc[index_questao - 1]['data_resposta'])
                        # print(hist['data_resposta'] - df_questoes_conjunto.iloc[index_questao - 1]['data_resposta'])
                        lista_tempo_resposta.append(
                            (hist['data_resposta'] - df_questoes_conjunto.iloc[index_questao - 1]['data_resposta']).dt.total_seconds()
                        )
            df_historico['tempo_resposta'] = lista_tempo_resposta
            return df_historico
        else:
            return None

    def calcula_taxa_esquecimento(self, id_usuario: int):
        questoes_respondidas = QuestaoUsuarioRepository.buscar_questoes_usuario_respondidas_por_id_usuario(self, id_usuario)
        colunas = {'qtd_repetidas': [0], 'dias_entre_questoes': [0], 'qtd_acertos': [0]}
        tabela_acertos = pd.DataFrame(colunas)
        for questao in questoes_respondidas:
            # print(questao.id_questao, questao.acerto)
            historico = self.calcula_tempo_resposta_historico_questao(id_usuario, questao.id_questao)
            if historico is not None and not historico.empty:
                if len(historico) > 1:
                    dias_entre_questoes = historico['data_resposta'].diff().dt.days.fillna(0).tolist()[1:]
                    # print(historico[['data_resposta', 'tempo_resposta']])
                    if tabela_acertos[tabela_acertos['dias_entre_questoes'] == dias_entre_questoes].empty:
                        tabela_acertos['dias_entre_questoes'] = dias_entre_questoes
                        tabela_acertos[tabela_acertos['dias_entre_questoes'] == dias_entre_questoes]['qtd_repetidas'] = 1
                        if questao.acerto:
                            tabela_acertos[tabela_acertos['dias_entre_questoes'] == dias_entre_questoes]['qtd_acertos'] = 1
                        else:
                            tabela_acertos[tabela_acertos['dias_entre_questoes'] == dias_entre_questoes]['qtd_acertos'] = 0
                    else:
                        tabela_acertos[tabela_acertos['dias_entre_questoes'] == dias_entre_questoes]['qtd_repetidas'] += 1
                        if questao.acerto:
                            tabela_acertos[tabela_acertos['dias_entre_questoes'] == dias_entre_questoes]['qtd_acertos'] += 1
                        else:
                            if (tabela_acertos[tabela_acertos['dias_entre_questoes'] == dias_entre_questoes]['qtd_acertos'] > 1).bool():
                                tabela_acertos[tabela_acertos['dias_entre_questoes'] == dias_entre_questoes]['qtd_acertos'] -= 1
                            else:
                                tabela_acertos[tabela_acertos['dias_entre_questoes'] == dias_entre_questoes]['qtd_acertos'] = 0
        if not tabela_acertos.empty:
            tabela_acertos['taxa_acerto'] = tabela_acertos['qtd_acertos'] / tabela_acertos['qtd_repetidas']
            # print(tabela_acertos)

        return tabela_acertos