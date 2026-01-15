from sqlalchemy import text

from models.objetivo import Objetivo


class ObjetivoRepository:
    def __init__(self, db):
        self.db = db
        
    def buscar_todos_objetivos(self):
        resultado = self.db.execute(text("""
            SELECT * FROM objetivo
        """)).all()

        objetivos = []
        for row in resultado:
            objetivos.append(Objetivo(
                id_objetivo=row.id_objetivo,
                descricao_objetivo=row.descricao_objetivo
            ))
        return objetivos