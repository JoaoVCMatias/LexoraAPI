from sqlalchemy.orm import Session
from sqlalchemy import text
from models.palavra import Palavra
from schemas.palavra import ObjetivoPalavras, PalavraCreate


class PalavraRepository:
    def __init__(self, db: Session):
        self.db = db

    def buscar_todas_palavras(self) -> list[Palavra]:
        rows = self.db.execute(text("""
            SELECT 
                id_palavra,
                descricao_palavra,
                descricao_palavra_traducao,
                "CEFR"
            FROM palavra
        """)).all()
        
        palavras = []
        for row in rows:
            palavras.append(
                Palavra(
                    id_palavra=row.id_palavra,
                    descricao_palavra=row.descricao_palavra,
                    descricao_palavra_traducao=row.descricao_palavra_traducao,
                    CEFR=row.CEFR
                )
            )
        return palavras

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
    
    def busca_palavras_por_objetivo_usuario(self, id_objetivo_usuario: int) -> list[PalavraCreate]:
        rows = self.db.execute(text("""
            SELECT 
                p.id_palavra,
                p.descricao_palavra,
                p.descricao_palavra_traducao,
                p."CEFR",
                b.descricao_objetivo
            FROM palavra p
            JOIN palavra_objetivo po ON po.id_palavra = p.id_palavra
            JOIN objetivo_usuario ou ON ou.id_objetivo = po.id_objetivo
            JOIN objetivo b ON b.id_objetivo = ou.id_objetivo
            WHERE ou.id_objetivo_usuario = :id_objetivo_usuario
        """), {"id_objetivo_usuario": id_objetivo_usuario}).all()

        # if rows:
        #     objetivo_palavras = ObjetivoPalavras(
        #         id_objetivo=id_objetivo_usuario,
        #         descricao_objetivo=rows[0].descricao_objetivo if rows else "",
        #         palavras=[
        #             PalavraCreate(
        #                 id_palavra=row.id_palavra,
        #                 descricao_palavra=row.descricao_palavra,
        #                 descricao_palavra_traducao=row.descricao_palavra_traducao,
        #                 CEFR=row.CEFR
        #             ) for row in rows
        #         ]
        #     ) 

        palavras = []
        if rows:
            for row in rows:
                palavras.append(
                    PalavraCreate(
                        id_palavra=row.id_palavra,
                        descricao_palavra=row.descricao_palavra,
                        descricao_palavra_traducao=row.descricao_palavra_traducao,
                        CEFR=row.CEFR
                    )
                )

        return palavras

    def pesquisa_palavra_por_descricao_ou_traducao(self, descricao_palavra: str) -> Palavra | None:
        descricao_palavra = f"%{descricao_palavra}%"
        palavras = []
        rows = self.db.execute(text("""
            SELECT 
                id_palavra,
                descricao_palavra,
                descricao_palavra_traducao,
                "CEFR"
            FROM palavra
            WHERE descricao_palavra ILIKE :descricao_palavra OR descricao_palavra_traducao ILIKE :descricao_palavra
        """), {"descricao_palavra": descricao_palavra}).all()
        
        for row in rows:
            palavras.append(Palavra(
                id_palavra=row.id_palavra,
                descricao_palavra=row.descricao_palavra,
                descricao_palavra_traducao=row.descricao_palavra_traducao,
                CEFR=row.CEFR
            ))
        
        return palavras
    
    def busca_palavra_por_descricao(self, descricao_palavra: str) -> Palavra | None:
        palavras = []
        rows = self.db.execute(text("""
            SELECT 
                id_palavra,
                descricao_palavra,
                descricao_palavra_traducao,
                "CEFR"
            FROM palavra
            WHERE descricao_palavra ILIKE :descricao_palavra
        """), {"descricao_palavra": descricao_palavra}).all()
        
        for row in rows:
            palavras.append(Palavra(
                id_palavra=row.id_palavra,
                descricao_palavra=row.descricao_palavra,
                descricao_palavra_traducao=row.descricao_palavra_traducao,
                CEFR=row.CEFR
            ))
        
        return palavras
    
    def buscar_palavra_por_traducao(self, palavra_traduzida: str) -> Palavra | None:
        palavras = []
        rows = self.db.execute(text("""
            SELECT 
                id_palavra,
                descricao_palavra,
                descricao_palavra_traducao,
                "CEFR"
            FROM palavra
            WHERE descricao_palavra_traducao ILIKE :palavra_traduzida
        """), {"palavra_traduzida": palavra_traduzida}).all()
        
        for row in rows:
            palavras.append(Palavra(
                id_palavra=row.id_palavra,
                descricao_palavra=row.descricao_palavra,
                descricao_palavra_traducao=row.descricao_palavra_traducao,
                CEFR=row.CEFR
            ))
        
        return palavras
    
    def busca_palavras_por_cefr(self, cefr: str) -> list[Palavra]:
        rows = self.db.execute(text("""
            SELECT 
                id_palavra,
                descricao_palavra,
                descricao_palavra_traducao,
                "CEFR"
            FROM palavra
            WHERE "CEFR" = :cefr
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