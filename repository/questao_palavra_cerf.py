from sqlalchemy import text


class QuestaoPalavraCERFRepository:
    def __init__(self, db):
        self.db = db

    def buscar_questao_palavra_cerf(self, id_questao: int):
        row = self.db.execute(text("""
            SELECT 
                id_questao,
                a1,
                a2,
                b1,
                b2,
                c1,
                c2
            FROM questao_palavra_cerf
            WHERE id_questao = :id_questao
        """), {"id_questao": id_questao}).first()
        
        if row:
            return {
                "id_questao": row.id_questao,
                "a1": row.a1,
                "a2": row.a2,
                "b1": row.b1,
                "b2": row.b2,
                "c1": row.c1,
                "c2": row.c2
            }
        
        return None

    def inserir_questao_palavra_cerf(self, id_questao: int, a1: int, a2: int, b1: int, b2: int, c1: int, c2: int):
        self.db.execute(text("""
            INSERT INTO questao_palavra_cerf (id_questao, a1, a2, b1, b2, c1, c2)
            VALUES (:id_questao, :a1, :a2, :b1, :b2, :c1, :c2)
        """), {"id_questao": id_questao, "a1": a1, "a2": a2, "b1": b1, "b2": b2, "c1": c1, "c2": c2})
        self.db.commit()