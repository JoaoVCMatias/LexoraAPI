from sqlalchemy import text
from models.conjunto_questao import ConjuntoQuestao


class ConjuntoQuestaoRepository:
    def __init__(self, db):
        self.db = db

    def buscar_conjunto_questoes_ativas_usuario(self, id_usuario: int):
        rows = self.db.execute(
            text("""
                SELECT 
                    cq.id_conjunto_questao,
                    cq.id_usuario,
                    cq.data_criacao,
                    cq.data_conclusao
                FROM conjunto_questao cq
                WHERE cq.id_usuario = :id_usuario AND cq.data_conclusao is null
            """), {"id_usuario": id_usuario}
        ).all()  

        conjuntos_ativos = []
        for row in rows:
            conjunto = ConjuntoQuestao(
                id_conjunto_questao=row.id_conjunto_questao,
                id_usuario=row.id_usuario,
                data_criacao=row.data_criacao,
                data_conclusao=row.data_conclusao
            )
            conjuntos_ativos.append(conjunto)

        return conjuntos_ativos
    
    def criar_conjunto_questao(self, id_usuario: int):
        novo_conjunto = ConjuntoQuestao(
            id_usuario=id_usuario,
            data_criacao=text("(SELECT NOW() AT TIME ZONE 'America/Sao_Paulo')")
        )
        self.db.add(novo_conjunto)
        self.db.commit()
        self.db.refresh(novo_conjunto)
        return novo_conjunto.id_conjunto_questao

    def buscar_conjuntos_finalizados_usuario(self, id_usuario: int):
        rows = self.db.execute(
            text("""
                SELECT 
                    cq.id_conjunto_questao,
                    cq.id_usuario,
                    cq.data_criacao,
                    cq.data_conclusao
                FROM conjunto_questao cq
                WHERE cq.id_usuario = :id_usuario AND cq.data_conclusao is not null
            """), {"id_usuario": id_usuario}
        ).all()  

        conjuntos_finalizados = []
        for row in rows:
            conjunto = ConjuntoQuestao(
                id_conjunto_questao=row.id_conjunto_questao,
                id_usuario=row.id_usuario,
                data_criacao=row.data_criacao,
                data_conclusao=row.data_conclusao
            )
            conjuntos_finalizados.append(conjunto)

        return conjuntos_finalizados
    
    def concluir_conjunto_questao(self, id_usuario: int, id_conjunto_questao: int, data_conclusao):
        self.db.execute(
            text("""
                UPDATE conjunto_questao
                SET data_conclusao = :data_conclusao
                WHERE id_conjunto_questao = :id_conjunto_questao AND id_usuario = :id_usuario
            """), {
                "data_conclusao": data_conclusao,
                "id_conjunto_questao": id_conjunto_questao,
                "id_usuario": id_usuario
            }
        )
        self.db.commit()

    def buscar_conjunto_questao_por_id(self, id_conjunto_questao: int) -> ConjuntoQuestao | None:
        row = self.db.execute(text("""
            SELECT 
                id_conjunto_questao,
                id_usuario,
                data_criacao,
                data_conclusao
            FROM conjunto_questao
            WHERE id_conjunto_questao = :id_conjunto_questao
        """), {"id_conjunto_questao": id_conjunto_questao}).first()
        
        if row:
            return ConjuntoQuestao(
                id_conjunto_questao=row.id_conjunto_questao,
                id_usuario=row.id_usuario,
                data_criacao=row.data_criacao,
                data_conclusao=row.data_conclusao
            )
        
        return row