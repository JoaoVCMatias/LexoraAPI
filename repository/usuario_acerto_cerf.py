from sqlalchemy import text

from models.usuario_acerto_cerf import UsuarioAcertoCERF


class UsuarioAcertoCERFRepository:
    def __init__(self, db):
        self.db = db

    def buscar_acertos_cerf_por_usuario(self, id_usuario: int):
        resultado = self.db.execute(text("""
            SELECT * FROM usuario_acerto_cerf
            WHERE id_usuario = :id_usuario
        """), {"id_usuario": id_usuario}).first()

        if resultado:
            return UsuarioAcertoCERF(
                id_usuario_acerto_cerf=resultado.id_usuario_acerto_cerf,
                id_usuario=resultado.id_usuario,
                a1=resultado.a1,
                a2=resultado.a2,
                b1=resultado.b1,
                b2=resultado.b2,
                c1=resultado.c1,
                c2=resultado.c2
            )
        return None