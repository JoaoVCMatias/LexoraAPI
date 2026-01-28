from sqlalchemy import text
from models.questao_palavra_cerf import QuestaoPalavraCerf


class QuestaoPalavraCERFRepository:
    def __init__(self, db):
        self.db = db

    def buscar_questao_palavra_cerf_por_id_questao(self, id_questao: int):
        row = self.db.execute(text("""
            SELECT 
                id_questao_palavra_cerf,
                id_questao,
                "A1",
                "A2",
                "B1",
                "B2",
                "C1",
                "C2"
            FROM questao_palavra_cerf
            WHERE id_questao = :id_questao
        """), {"id_questao": id_questao}).first()
        
        if row:
            return QuestaoPalavraCerf(
                id_questao_palavra_cerf=row.id_questao_palavra_cerf,
                id_questao=row.id_questao,
                A1=row.A1,
                A2=row.A2,
                B1=row.B1,
                B2=row.B2,
                C1=row.C1,
                C2=row.C2
            )
        
        return None

    def inserir_questao_palavra_cerf(self, id_questao: int, a1: int, a2: int, b1: int, b2: int, c1: int, c2: int):
        query = "INSERT INTO questao_palavra_cerf (id_questao, \"A1\", \"A2\", \"B1\", \"B2\", \"C1\", \"C2\") VALUES ("+str(id_questao)+", "+str(a1)+", "+str(a2)+", "+str(b1)+", "+str(b2)+", "+str(c1)+", "+str(c2)+")"
        return query

        self.db.execute(text("""
            INSERT INTO questao_palavra_cerf (id_questao, "A1", "A2", "B1", "B2", "C1", "C2")
            VALUES (:id_questao, :a1, :a2, :b1, :b2, :c1, :c2)
        """), {"id_questao": id_questao, "a1": a1, "a2": a2, "b1": b1, "b2": b2, "c1": c1, "c2": c2})
        self.db.commit()