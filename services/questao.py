from fastapi import  HTTPException
from repository.questao import QuestaoRepository
from sqlalchemy.orm import Session
from datetime import date
from datetime import datetime
from repository.usuario import UsuarioRepository
import json

class QuestaoService:

    def __init__(self, db: Session):
        self.db = db

    def buscar_questoes_usuario(self, id_usuario: int):
        print(id_usuario)
        return QuestaoRepository.buscar_questoes_usuario(self, id_usuario)
    
    def gerar_questao_id(self, id_usuario: int):
        questoes_usuario = self.buscar_questoes_usuario(id_usuario)
        if questoes_usuario is not None and len(questoes_usuario.questoes) > 0:
            return questoes_usuario
        
        date_atual = datetime.now()
        ids_questao = QuestaoRepository.buscar_questoes(self, id_usuario, 5, 2)
        id_conjunto = QuestaoRepository.inserir_conjunto_questoes(self, id_usuario, date_atual)

        QuestaoRepository.inserir_questao_usuario(self, id_usuario, ids_questao, id_conjunto, date_atual) 
        return self.buscar_questoes_usuario(id_usuario)

    def responder_questao(self, id_usuario: int, id_questao: int, alternariva: int, id_conjunto_questao: int):
        usuario = UsuarioRepository.buscar_usuario_por_id(self, id_usuario)
        if not usuario:
            return {"erro": "Usuário não encontrado."}
        
        questoes_usuario = QuestaoRepository.buscar_questoes_usuario(self, id_usuario).questoes
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
        
        print(alterenativas_questao[alternariva], questao.resposta)
        
        data_resposta = datetime.now()

        QuestaoRepository.responder_questao(self, id_usuario, id_questao, correta, id_conjunto_questao, data_resposta)
        if conclusao:
            QuestaoRepository.concluir_conjunto_questoes(self, id_conjunto_questao, data_resposta)

        return correta 

    