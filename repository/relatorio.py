from sqlalchemy.orm import Session
from sqlalchemy import text
from schemas.relatorio import RelatorioEstatiticas, RelatorioDataUsuario, RelatorioAtividadeUsuario

class RelatorioRepository:
    def __init__(self, db: Session):
        self.db = db
    
    def buscar_relatorio_estatistica_usuario(self, id_usuario: int) -> RelatorioEstatiticas | None:
        row = self.db.execute(text("""
            ;WITH RelacaoCompleta AS (
	            SELECT 
	            	cq.id_conjunto_questao,
	            	cq.id_usuario,
	            	cq.data_criacao,
	            	qu.id_questao_usuario,
	            	qu.acerto,
	            	q.nivel 
	            FROM conjunto_questao cq
	            INNER JOIN questao_usuario qu 
	            	ON qu.id_conjunto_questao  = cq.id_conjunto_questao 
	            INNER JOIN questao q 
	            	ON q.id_questao  = qu.id_questao 
	            WHERE cq.id_usuario  = :id_usuario
	            AND cq.data_conclusao IS NOT NULL 
            ), UltimoConjuntoRealizado AS (
             	SELECT rc.id_usuario , max(rc.data_criacao) AS data_ultima_atividade 
            	FROM RelacaoCompleta rc
            	GROUP BY rc.id_usuario
            ), DiasAtivos AS (
            	SELECT 
            		sq.id_usuario, 
            		count(sq.id_usuario) AS dias_ativos
            	FROM (
            		SELECT 
            			rc.id_usuario,
            			COUNT(rc.id_usuario )
            		FROM RelacaoCompleta rc
            		GROUP BY rc.id_usuario, date(data_criacao)
            	) AS sq 
            	GROUP BY sq.id_usuario
            ), AtividadesFeitas AS (
            	SELECT rc.id_usuario, COUNT(rc.id_conjunto_questao) AS atividades_feitas 
            	FROM RelacaoCompleta rc
            	GROUP BY rc.id_usuario 
            ), TotalPontos AS (
            	SELECT 
            		rc.id_usuario, 
            		SUM(rc.nivel * 100) AS pontos_totais  
            	FROM RelacaoCompleta rc
            	GROUP BY rc.id_usuario
            ), Sequencias AS (
            	SELECT 
            		rc.id_questao_usuario, 
            		rc.id_conjunto_questao,
            		rc.data_criacao,
            		RC.id_usuario,
            		rc.acerto,
                    SUM(CASE WHEN rc.acerto  = FALSE THEN 1 ELSE 0 END) 
                    OVER (ORDER BY rc.id_questao_usuario) AS grupo
                FROM RelacaoCompleta rc
            ), MaiorSequenciaGeral AS (
            	SELECT sub.id_usuario, MAX(contagem) AS maior_sequencia
                FROM (
                		SELECT id_usuario, grupo, COUNT(*) AS contagem
                    	FROM Sequencias
                    	WHERE acerto = TRUE
                    GROUP BY id_usuario, grupo
                	) sub
                	GROUP BY sub.id_usuario 
             ), UltimaSequencia AS ( 	
             	SELECT sub.id_usuario, MAX(contagem) AS ultima_sequencia
                FROM (
                		SELECT s.id_usuario, grupo, COUNT(*) AS contagem
                    	FROM Sequencias s 
                    	INNER JOIN UltimoConjuntoRealizado  ucr
                    		ON ucr.id_usuario = s.id_usuario 
                    		AND ucr.data_ultima_atividade = s.data_criacao 
                    	WHERE acerto = TRUE
                    GROUP BY s.id_usuario, grupo
                	) sub
                	GROUP BY sub.id_usuario 
            ) SELECT
            	da.id_usuario,
            	da.dias_ativos,
            	af.atividades_feitas,
            	tp.pontos_totais,
            	us.ultima_sequencia,
            	msg.maior_sequencia 
            FROM DiasAtivos da
            INNER JOIN AtividadesFeitas af
            	ON af.id_usuario  = da.id_usuario 
            INNER JOIN TotalPontos tp
            	ON tp.id_usuario = da.id_usuario 
            INNER JOIN UltimaSequencia us
            	ON us.id_usuario = da.id_usuario 
            INNER JOIN MaiorSequenciaGeral msg
            	ON msg.id_usuario  = da.id_usuario 
        """), {"id_usuario": id_usuario}).first()
        
        if row:
            return RelatorioEstatiticas(
                id_usuario=row.id_usuario,
                dias_ativo=row.dias_ativos,
                atividades_feitas=row.atividades_feitas,
                pontos_totais=row.pontos_totais,
                maior_sequencia=row.maior_sequencia,
                ultima_sequencia=row.ultima_sequencia
            )
        return None
    
    def buscar_relatorio_data_usuario(self, id_usuario: int) -> list[RelatorioDataUsuario] | None:
        row = self.db.execute(text("""
            ;WITH CalendarioMes AS (
	            SELECT generate_series(
                		date_trunc('month', current_date)::date,                   -- primeiro dia do mês atual
                		(date_trunc('month', current_date) 
                    		+ interval '1 month - 1 day')::date,         -- último dia do mês atual
                		interval '1 day'
	            )::date AS dia
            ), Data15Dias AS (
            	SELECT (current_date - INTERVAL '15 days')::date AS data_menos_15
            ), CalcularPontos15 AS (
            	SELECT (cq.data_criacao::date) AS data, 
            	COALESCE(SUM(q.nivel * 100), 0) AS pontos
            	FROM conjunto_questao cq 
            	LEFT  JOIN questao_usuario qu 
            		ON qu.id_conjunto_questao  = cq.id_conjunto_questao 
            		AND qu.acerto = TRUE
            	LEFT JOIN questao q 
            		ON q.id_questao  = qu.id_questao
            	LEFT  JOIN Data15Dias  d
            		ON d.data_menos_15 <= cq.data_criacao
            	WHERE cq.id_usuario  = :id_usuario
            	GROUP BY  cq.data_criacao
            )SELECT DISTINCT 
            	cm.dia, 
            	CASE WHEN cq.data_conclusao IS NOT NULL THEN TRUE ELSE FALSE END AS Feito,
            	COALESCE(cp.pontos, 0) AS pontos 
            FROM CalendarioMes cm
            LEFT JOIN conjunto_questao cq 
            	ON cq.data_criacao = cm.dia 
            	AND cq.data_conclusao IS NOT NULL
            LEFT JOIN CalcularPontos15 cp
            	ON cp.DATA = cm.dia 
            ORDER BY cm.dia
        """), {"id_usuario": id_usuario}).all()

        if row:
            relatorio_data = []
            for r in row:
                relatorio_data.append(
                    RelatorioDataUsuario(
                        data=str(r.dia),
                        pontos=int(r.pontos)
                    )
                )
            return relatorio_data

        return None

    def buscar_metas_usuario(self, id_usuario: int) -> RelatorioAtividadeUsuario | None:
        row = self.db.execute(text("""
            SELECT 
	            CASE 
	            	WHEN u.id_disponibilidade = 1 THEN 5  
	            	WHEN u.id_disponibilidade = 2 THEN 10  
	            	WHEN u.id_disponibilidade = 3 THEN 15  
	            	ELSE  0
	            END AS meta,
	            COUNT(qu.id_questao) atividades_realizadas
            FROM usuario u
            LEFT JOIN conjunto_questao cq 
            	ON cq.id_usuario  = u.id_usuario 
            	AND cq.data_criacao::date = now()::date
            	AND cq.data_conclusao  IS NOT NULL 
            LEFT JOIN questao_usuario qu 
            	ON qu.id_conjunto_questao  = cq.id_conjunto_questao 
            WHERE u.id_usuario = :id_usuario
            GROUP BY u.id_disponibilidade
        """), {"id_usuario": id_usuario}).first()

        if row:
            return RelatorioAtividadeUsuario(
                meta=row.meta,
                atividades_feitas=row.atividades_realizadas
            )
        return None 