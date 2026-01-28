from sqlalchemy.orm import Session
from sqlalchemy import text
from datetime import date
from schemas.usuario import UsuarioQuestaoReturn, QuestoesUsuarioResponse, RelatorioDesempenhoUsuarioResponse
from models.questao import Questao

class QuestaoRepository:

    def __init__(self, db: Session):
        self.db = db

    def buscar_todas_questoes(self) -> list[Questao]:
        rows = self.db.execute(text("""
            SELECT 
                id_questao,
                descricao_questao,
                json_opcao,
                resposta 
            FROM questao
        """)).all()
        
        questoes = []
        for row in rows:
            questoes.append(
                Questao(
                    id_questao=row.id_questao,
                    descricao_questao=row.descricao_questao,
                    json_opcao=row.json_opcao,
                    resposta=row.resposta
                )
            )
        return questoes

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
            and (qu.acerto is null or (qu.acerto = FALSE and  qu.data_resposta + INTERVAL '1 day' > (SELECT NOW() AT TIME ZONE 'America/Sao_Paulo'))
            or  (qu.acerto = TRUE and  qu.data_resposta + INTERVAL '3 day' > (SELECT NOW() AT TIME ZONE 'America/Sao_Paulo')))
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

    def buscar_questoes_usuario(self, id_usuario: int, id_conjunto_questao: int|None) -> UsuarioQuestaoReturn | None:
        rows = self.db.execute(text(f"""
            SELECT 
                cq.id_conjunto_questao, 
                q.id_questao, 
                q.descricao_questao,                  
                q.json_opcao, 
                qu.acerto,
                CASE 
		            WHEN qu.acerto IS NOT NULL THEN q.resposta
		            ELSE NULL
	            END AS resposta,
                qu.resposta_usuario
            FROM conjunto_questao cq 
            INNER JOIN questao_usuario qu 
                ON qu.id_usuario = cq.id_usuario 
                AND qu.id_conjunto_questao = cq.id_conjunto_questao
            LEFT JOIN questao q 
                ON q.id_questao = qu.id_questao 
            WHERE cq.id_usuario = :id_usuario
            {f"AND cq.id_conjunto_questao = :id_conjunto_questao" if id_conjunto_questao is not None else "AND cq.data_conclusao IS NULL"}
            ORDER BY cq.id_conjunto_questao, q.id_questao
        """), {"id_usuario": id_usuario, "id_conjunto_questao": id_conjunto_questao}).all()
        if not rows:
            return None

        conjunto = UsuarioQuestaoReturn(
            id_conjunto_questao=rows[0].id_conjunto_questao,
            questoes=[
                QuestoesUsuarioResponse(
                    id_questao=row.id_questao,
                    descricao_questao=row.descricao_questao,
                    json_opcao=row.json_opcao,
                    acerto=row.acerto,
                    resposta=row.resposta,
                    resposta_usuario=row.resposta_usuario
                )
                for row in rows
            ]
        )

        return conjunto
    
    def responder_questao(self, id_usuario: int, id_questao: int, correta: bool, resposta_usuario: str, id_conjunto_questao: int, data_resposta: date):
        print("id_usuario:", id_usuario, "id_questao:", id_questao, "correta:", correta, "id_conjunto_questao:", id_conjunto_questao)
        self.db.execute(text("""
            UPDATE questao_usuario
            SET acerto = :acerto,
                data_resposta = :data_resposta,
                resposta_usuario = :resposta_usuario
            WHERE id_usuario = :id_usuario
            AND id_questao = :id_questao
            AND id_conjunto_questao = :id_conjunto_questao
            AND data_resposta IS NULL
        """), {"acerto": correta, "resposta_usuario": resposta_usuario, "data_resposta": data_resposta, "id_usuario": id_usuario, "id_questao": id_questao, "id_conjunto_questao": id_conjunto_questao})
        self.db.commit()    

    def concluir_conjunto_questoes(self, id_conjunto_questao: int, data_conclusao: date):
        self.db.execute(text("""
            UPDATE conjunto_questao
            SET data_conclusao = :data_conclusao
            WHERE id_conjunto_questao = :id_conjunto_questao
            AND data_conclusao IS NULL
        """), {"id_conjunto_questao": id_conjunto_questao, "data_conclusao": data_conclusao})
        self.db.commit()

    def relatorio_desenpenho_usuario(self, id_usuario: int) -> list[RelatorioDesempenhoUsuarioResponse] | None:
        rows = self.db.execute(text("""
            ;WITH ConjuntoQuestaoUsuario AS (
	            SELECT 
	            	MAX(cq.id_conjunto_questao) AS id_conjunto_questao 
	            FROM conjunto_questao cq 
	            WHERE cq.id_usuario = :id_usuario 
	            AND cq.data_conclusao IS NOT NULL
            ), Sequencias AS (
                SELECT qu.id_questao_usuario, qu.acerto,
                       SUM(CASE WHEN qu.acerto  = FALSE THEN 1 ELSE 0 END) 
                           OVER (ORDER BY qu.id_questao_usuario) AS grupo
                FROM questao_usuario qu 
                INNER JOIN ConjuntoQuestaoUsuario CQU
                	ON CQU.id_conjunto_questao  = QU.id_conjunto_questao 
            ), MaiorSequencia AS (
            	SELECT MAX(contagem) AS maior_sequencia
            	FROM (
                	SELECT grupo, COUNT(*) AS contagem
                	FROM Sequencias
                	WHERE acerto = TRUE
                	GROUP BY grupo
            	) sub
            )
            SELECT 
                cqu.id_conjunto_questao,
            	AGE(cq.data_conclusao, cq.data_criacao) AS tempo,
            	COALESCE(SUM(q.nivel * 100), 0) AS pontos,
            	(CAST(SUM(CASE WHEN qu.acerto = TRUE THEN 1 ELSE 0 END) AS DECIMAL) / CAST(COUNT(qu.id_questao) AS DECIMAL)) * 100 
            	AS porcentagem_acerto,
            	COALESCE((SELECT maior_sequencia FROM MaiorSequencia), 0) AS sequencia_acerto
            FROM ConjuntoQuestaoUsuario cqu
            INNER JOIN conjunto_questao cq 
            	ON cq.id_conjunto_questao = cqu.id_conjunto_questao
            INNER JOIN questao_usuario qu 
            	ON qu.id_conjunto_questao  = cqu.id_conjunto_questao
            LEFT JOIN questao q 
            	ON q.id_questao = qu.id_questao
            	AND QU.acerto = TRUE
            GROUP BY 
                cqu.id_conjunto_questao,                        
            	cq.data_criacao,
            	cq.data_conclusao
        """), {"id_usuario": id_usuario}).all()

        if not rows:
            return None
        
        relatorio = []
        for row in rows:
            relatorio.append(
                RelatorioDesempenhoUsuarioResponse(
                    id_conjunto_questao=row.id_conjunto_questao,
                    tempo=str(row.tempo),
                    pontos=float(row.pontos),
                    porcentagem_acerto=float(row.porcentagem_acerto),
                    sequencia_acerto=int(row.sequencia_acerto),
                    questoes=[] 
                )
            )
        return relatorio

    def resultado_conjunto_questoes(self, id_usuario: int, id_conjunto: int) -> list[RelatorioDesempenhoUsuarioResponse] | None:
        rows = self.db.execute(text("""
            ;WITH ConjuntoQuestaoUsuario AS (
	            SELECT 
	            	MAX(cq.id_conjunto_questao) AS id_conjunto_questao 
	            FROM conjunto_questao cq 
	            WHERE cq.id_usuario = :id_usuario 
                AND cq.id_conjunto_questao = :id_conjunto
	            AND cq.data_conclusao IS NOT NULL
            ), Sequencias AS (
                SELECT qu.id_questao_usuario, qu.acerto,
                       SUM(CASE WHEN qu.acerto  = FALSE THEN 1 ELSE 0 END) 
                           OVER (ORDER BY qu.id_questao_usuario) AS grupo
                FROM questao_usuario qu 
                INNER JOIN ConjuntoQuestaoUsuario CQU
                	ON CQU.id_conjunto_questao  = QU.id_conjunto_questao 
            ), MaiorSequencia AS (
            	SELECT MAX(contagem) AS maior_sequencia
            	FROM (
                	SELECT grupo, COUNT(*) AS contagem
                	FROM Sequencias
                	WHERE acerto = TRUE
                	GROUP BY grupo
            	) sub
            )
            SELECT 
                cqu.id_conjunto_questao,
            	AGE(cq.data_conclusao, cq.data_criacao) AS tempo,
            	COALESCE(SUM(q.nivel * 100), 0) AS pontos,
            	(CAST(SUM(CASE WHEN qu.acerto = TRUE THEN 1 ELSE 0 END) AS DECIMAL) / CAST(COUNT(qu.id_questao) AS DECIMAL)) * 100 
            	AS porcentagem_acerto,
            	COALESCE((SELECT maior_sequencia FROM MaiorSequencia), 0) AS sequencia_acerto
            FROM ConjuntoQuestaoUsuario cqu
            INNER JOIN conjunto_questao cq 
            	ON cq.id_conjunto_questao = cqu.id_conjunto_questao
            INNER JOIN questao_usuario qu 
            	ON qu.id_conjunto_questao  = cqu.id_conjunto_questao
            LEFT JOIN questao q 
            	ON q.id_questao = qu.id_questao
            	AND QU.acerto = TRUE
            GROUP BY 
                cqu.id_conjunto_questao,                        
            	cq.data_criacao,
            	cq.data_conclusao
        """), {"id_usuario": id_usuario, "id_conjunto": id_conjunto}).all()

        if not rows:
            return None
        
        relatorio = []
        for row in rows:
            relatorio.append(
                RelatorioDesempenhoUsuarioResponse(
                    id_conjunto_questao=row.id_conjunto_questao,
                    tempo=str(row.tempo),
                    pontos=float(row.pontos),
                    porcentagem_acerto=float(row.porcentagem_acerto),
                    sequencia_acerto=int(row.sequencia_acerto),
                    questoes=[] 
                )
            )
        return relatorio