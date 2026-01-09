from sqlalchemy.orm import Session
from sqlalchemy import text
from models.palavra import Palavra


class PalavraRepository:
    def __init__(self, db: Session):
        self.db = db

    def buscar_palavra_por_id(self, id_palavra: int) -> Palavra | None:
        row = self.db.execute(text("""
            SELECT 
                id_palavra,
                descricao_palavra,
                descricao_palavra_traducao
            FROM palavra
            WHERE id_palavra = :id_palavra
        """), {"id_palavra": id_palavra}).first()
        
        if row:
            return Palavra(
                id_palavra=row.id_palavra,
                descricao_palavra=row.descricao_palavra,
                descricao_palavra_traducao=row.descricao_palavra_traducao,
                # CEFR=row.CEFR
            )
        
        return None
    
    def busca_palavras_por_objetivo_usuario(self, id_objetivo_usuario: int) -> list[Palavra]:
        rows = self.db.execute(text("""
            SELECT 
                p.id_palavra,
                p.descricao_palavra,
                p.descricao_palavra_traducao,
                p.CEFR
            FROM palavra p
            JOIN palavra_objetivo po ON po.id_palavra = p.id_palavra
            JOIN objetivo_usuario ou ON ou.id_objetivo = po.id_objetivo
            WHERE ou.id_objetivo_usuario = :id_objetivo_usuario
        """), {"id_objetivo_usuario": id_objetivo_usuario}).all()
        
        palavras = []
        for row in rows:
            palavras.append(Palavra(
                id_palavra=row.id_palavra,
                descricao_palavra=row.descricao_palavra,
                descricao_palavra_traducao=row.descricao_palavra_traducao,
                CEFR=row.CEFR
            ))
        
        return palavras
    
    def busca_palavra_por_descricao(self, descricao_palavra: str) -> Palavra | None:
        row = self.db.execute(text("""
            SELECT 
                id_palavra,
                descricao_palavra,
                descricao_palavra_traducao,
                CEFR
            FROM palavra
            WHERE descricao_palavra = :descricao_palavra
        """), {"descricao_palavra": descricao_palavra}).first()
        
        if row:
            return Palavra(
                id_palavra=row.id_palavra,
                descricao_palavra=row.descricao_palavra,
                descricao_palavra_traducao=row.descricao_palavra_traducao,
                CEFR=row.CEFR
            )
        
        return None
    
    def busca_palavras_por_cefr(self, cefr: str) -> list[Palavra]:
        rows = self.db.execute(text("""
            SELECT 
                id_palavra,
                descricao_palavra,
                descricao_palavra_traducao,
                CEFR
            FROM palavra
            WHERE CEFR = :cefr
        """), {"cefr": cefr}).all()
        
        palavras = []
        for row in rows:
            palavras.append(Palavra(
                id_palavra=row.id_palavra,
                descricao_palavra=row.descricao_palavra,
                descricao_palavra_traducao=row.descricao_palavra_traducao,
                CEFR=row.CEFR
            ))
        
        return palavras