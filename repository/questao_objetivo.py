from sqlalchemy import text

from models.questao_objetivo import QuestaoObjetivo


class QuestaoObjetivoRepository:
    def __init__(self, db):
        self.db = db

    def inserir_questao_objetivo(self, id_questao: int, id_objetivo: int, qtq_palavras: int):
        self.db.execute(text("""
            INSERT INTO questao_objetivo (id_questao, id_objetivo, qtq_palavras)
            VALUES (:id_questao, :id_objetivo, :qtq_palavras)
        """), {"id_questao": id_questao, "id_objetivo": id_objetivo, "qtq_palavras": qtq_palavras})
        self.db.commit()

    def buscar_questao_objetivo(self, id_questao: int, id_objetivo: int):
        row = self.db.execute(text("""
            SELECT 
                id_questao_objetivo,
                id_questao,
                id_objetivo,
                qtq_palavras
            FROM questao_objetivo
            WHERE id_questao = :id_questao AND id_objetivo = :id_objetivo
        """), {"id_questao": id_questao, "id_objetivo": id_objetivo}).first()
        
        if row:
            return QuestaoObjetivo(
                id_questao_objetivo=row.id_questao_objetivo,
                id_questao=row.id_questao,
                id_objetivo=row.id_objetivo,
                qtq_palavras=row.qtq_palavras
            )
        
        return row
    
    def buscar_questoes_por_objetivo(self, id_objetivo: int):
        rows = self.db.execute(text("""
            SELECT 
                id_questao_objetivo,
                id_questao,
                id_objetivo,
                qtq_palavras
            FROM questao_objetivo
            WHERE id_objetivo = :id_objetivo
        """), {"id_objetivo": id_objetivo}).all()
        
        questoes_objetivo = []
        for row in rows:
            questoes_objetivo.append(QuestaoObjetivo(
                id_questao_objetivo=row.id_questao_objetivo,
                id_questao=row.id_questao,
                id_objetivo=row.id_objetivo,
                qtq_palavras=row.qtq_palavras
            ))
        
        return questoes_objetivo