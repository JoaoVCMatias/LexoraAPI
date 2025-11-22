from sqlalchemy.orm import Session
from sqlalchemy import text
from datetime import date
from schemas.usuario import UsuarioQuestaoReturn, QuestoesUsuarioResponse
from models.questao import Questao

class QuestaoRepository:

    def __init__(self, db: Session):
        self.db = db

    def buscar_questao_por_id(self, id_questao: int) -> Questao | None:
        row = self.db.execute(text("""
            SELECT 
                id_questao,
                descricao_questao,
                json_opcao,
                resposta 
            FROM questao
            WHERE id_questao = :id_questao
        """), {"id_questao": id_questao}).first()
        
        if row:
            return Questao(
                id_questao=row.id_questao,
                descricao_questao=row.descricao_questao,
                json_opcao=row.json_opcao,
                resposta=row.resposta
            )
        
        return None
    
    def buscar_questoes(self, id_usuario: int, qnt_questoes: int, id_tipo_questao: int):
        row = self.db.execute(text(""" 
            select 
	            q.id_questao
            from questao q 
            left join questao_usuario qu 
	            on qu.id_questao  = q.id_questao 
	            and qu.id_usuario = :id_usuario
            where q.id_tipo_questao = :id_tipo_questao
            and (qu.acerto is null or (qu.acerto = FALSE and  qu.data_resposta + INTERVAL '1 day' > CURRENT_DATE)
            or  (qu.acerto = TRUE and  qu.data_resposta + INTERVAL '3 day' > CURRENT_DATE))
            order by random()
            limit :qnt_questoes"""), {"id_usuario": id_usuario, "qnt_questoes": qnt_questoes, "id_tipo_questao": id_tipo_questao}).all()
        
        return [row_item.id_questao for row_item in row]
    
 

    def inserir_conjunto_questoes(self, id_usuario: int, data_atual: date) -> int:
        result = self.db.execute(text("""
            INSERT INTO conjunto_questao (id_usuario, data_criacao)
            VALUES (:id_usuario, :data_criacao)
            RETURNING id_conjunto_questao
        """), {"id_usuario": id_usuario, "data_criacao": data_atual})
    
        inserted_id = result.scalar()
    
        self.db.commit()
        return inserted_id

    def inserir_questao_usuario(self, id_usuario: int, ids_questao: list[int], id_conjunto: int, data_criacao: date):  
        for id_questao in ids_questao:
            self.db.execute(text("""
                INSERT INTO questao_usuario (id_usuario, id_questao, id_conjunto_questao, data_criacao)
                VALUES (:id_usuario, :id_questao, :id_conjunto, :data_criacao)
            """), {"id_usuario": id_usuario, "id_questao": id_questao,  "id_conjunto": id_conjunto, "data_criacao": data_criacao})
        self.db.commit()

    def buscar_questoes_usuario(self, id_usuario: int) -> UsuarioQuestaoReturn | None:
        print(id_usuario)
        rows = self.db.execute(text("""
            SELECT 
                cq.id_conjunto_questao, 
                q.id_questao, 
                q.descricao_questao,                  
                q.json_opcao, 
                qu.acerto 
            FROM conjunto_questao cq 
            INNER JOIN questao_usuario qu 
                ON qu.id_usuario = cq.id_usuario 
                AND qu.id_conjunto_questao = cq.id_conjunto_questao
            INNER JOIN questao q 
                ON q.id_questao = qu.id_questao 
            WHERE cq.id_usuario = :id_usuario
            AND cq.data_conclusao IS NULL
        """), {"id_usuario": id_usuario}).all()

        if not rows:
            return None

        conjunto = UsuarioQuestaoReturn(
            id_conjunto_questao=rows[0].id_conjunto_questao,
            questoes=[
                QuestoesUsuarioResponse(
                    id_questao=row.id_questao,
                    descricao_questao=row.descricao_questao,
                    json_opcao=row.json_opcao,
                    acerto=row.acerto
                )
                for row in rows
            ]
        )

        return conjunto
    
    def responder_questao(self, id_usuario: int, id_questao: int, correta: bool, id_conjunto_questao: int, data_resposta: date):
        print("id_usuario:", id_usuario, "id_questao:", id_questao, "correta:", correta, "id_conjunto_questao:", id_conjunto_questao)
        self.db.execute(text("""
            UPDATE questao_usuario
            SET acerto = :acerto,
                data_resposta = :data_resposta
            WHERE id_usuario = :id_usuario
            AND id_questao = :id_questao
            AND id_conjunto_questao = :id_conjunto_questao
            AND data_resposta IS NULL
        """), {"acerto": correta, "data_resposta": data_resposta, "id_usuario": id_usuario, "id_questao": id_questao, "id_conjunto_questao": id_conjunto_questao})
        self.db.commit()    

    def concluir_conjunto_questoes(self, id_conjunto_questao: int, data_conclusao: date):
        self.db.execute(text("""
            UPDATE conjunto_questao
            SET data_conclusao = :data_conclusao
            WHERE id_conjunto_questao = :id_conjunto_questao
            AND data_conclusao IS NULL
        """), {"id_conjunto_questao": id_conjunto_questao, "data_conclusao": data_conclusao})
        self.db.commit()
    