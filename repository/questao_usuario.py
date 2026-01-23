from sqlalchemy import text
from models.questao_usuario import QuestaoUsuario


class QuestaoUsuarioRepository:
    def __init__(self, db):
        self.db = db
    
    def buscar_questoes_usuario(self, id_usuario: int, id_conjunto_questao: int = None):
        query = """
            SELECT 
                qu.id_questao_usuario,
                qu.id_usuario,
                qu.id_questao,
                qu.id_conjunto_questao,
                qu.data_resposta,
                qu.acerto
            FROM questao_usuario qu
            WHERE qu.id_usuario = :id_usuario
        """
        params = {"id_usuario": id_usuario}
        
        if id_conjunto_questao is not None:
            query += " AND qu.id_conjunto_questao = :id_conjunto_questao"
            params["id_conjunto_questao"] = id_conjunto_questao
        
        rows = self.db.execute(text(query), params).all()
        
        questoes_usuario = []
        for row in rows:
            questoes_usuario.append(
                QuestaoUsuario(
                    id_questao_usuario=row.id_questao_usuario,
                    id_usuario=row.id_usuario,
                    id_questao=row.id_questao,
                    id_conjunto_questao=row.id_conjunto_questao,
                    data_resposta=row.data_resposta,
                    acerto=row.acerto
                )
            )
        return questoes_usuario
    
    def criar_questao_usuario(self, id_usuario: int, id_questao: int, id_conjunto_questao: int):
        nova_questao_usuario = QuestaoUsuario(
            id_usuario=id_usuario,
            id_questao=id_questao,
            id_conjunto_questao=id_conjunto_questao,
            data_criacao=text("CURRENT_DATE")
        )
        self.db.add(nova_questao_usuario)
        self.db.commit()
        self.db.refresh(nova_questao_usuario)
        return nova_questao_usuario.id_questao_usuario
    
    def buscar_questoes_por_conjunto_id(self, id_conjunto_questao: int):
        rows = self.db.execute(
            text("""
                SELECT 
                    qu.id_questao_usuario,
                    qu.id_usuario,
                    qu.id_questao,
                    qu.id_conjunto_questao,
                    qu.data_resposta,
                    qu.acerto
                FROM questao_usuario qu
                WHERE qu.id_conjunto_questao = :id_conjunto_questao
            """), {"id_conjunto_questao": id_conjunto_questao}
        ).all()
        
        questoes_usuario = []
        for row in rows:
            questoes_usuario.append(
                QuestaoUsuario(
                    id_questao_usuario=row.id_questao_usuario,
                    id_usuario=row.id_usuario,
                    id_questao=row.id_questao,
                    id_conjunto_questao=row.id_conjunto_questao,
                    data_resposta=row.data_resposta,
                    acerto=row.acerto
                )
            )
        return questoes_usuario
    
    def buscar_questao_usuario_por_id_usuario(self, id_usuario: int):
        rows = self.db.execute(text("""
            SELECT 
                qu.id_questao_usuario,
                qu.id_usuario,
                qu.id_questao,
                qu.id_conjunto_questao,
                qu.data_resposta,
                qu.acerto
            FROM questao_usuario qu
            WHERE qu.id_usuario = :id_usuario
        """), {"id_usuario": id_usuario}).all()
        
        questoes_usuario = []
        for row in rows:
            questoes_usuario.append(
                QuestaoUsuario(
                    id_questao_usuario=row.id_questao_usuario,
                    id_usuario=row.id_usuario,
                    id_questao=row.id_questao,
                    id_conjunto_questao=row.id_conjunto_questao,
                    data_resposta=row.data_resposta,
                    acerto=row.acerto
                )
            )
        return questoes_usuario
    
    def buscar_questoes_usuario_respondidas_por_id_usuario(self, id_usuario: int):
        rows = self.db.execute(text("""
            SELECT 
                qu.id_questao_usuario,
                qu.id_usuario,
                qu.id_questao,
                qu.id_conjunto_questao,
                qu.data_resposta,
                qu.acerto
            FROM questao_usuario qu
            WHERE qu.id_usuario = :id_usuario
            and qu.data_resposta is not null
        """), {"id_usuario": id_usuario}).all()
        
        questoes_usuario = []
        for row in rows:
            questoes_usuario.append(
                QuestaoUsuario(
                    id_questao_usuario=row.id_questao_usuario,
                    id_usuario=row.id_usuario,
                    id_questao=row.id_questao,
                    id_conjunto_questao=row.id_conjunto_questao,
                    data_resposta=row.data_resposta,
                    acerto=row.acerto
                )
            )
        return questoes_usuario