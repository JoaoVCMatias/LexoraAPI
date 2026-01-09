from sqlalchemy.orm import Session
from sqlalchemy import text


class PalavraObjetivoRepository:
    def __init__(self, db: Session):
        self.db = db

    def buscar_id_palavras_por_id_objetivo(self, id_objetivo: int) -> list[int] | None:
        rows = self.db.execute(text("""
            SELECT 
                id_palavra
            FROM palavra_objetivo
            WHERE id_objetivo = :id_objetivo
        """), {"id_objetivo": id_objetivo}).all()
        
        return [row.id_palavra for row in rows]
        # return None

    def buscar_palavras_objetivo_por_id_objetivo(self, id_objetivo: int) -> list[int]:
        rows = self.db.execute(text("""
            SELECT 
                id_palavra
            FROM palavra_objetivo
            WHERE id_objetivo = :id_objetivo
        """), {"id_objetivo": id_objetivo}).all()
        
        return rows
        # return None