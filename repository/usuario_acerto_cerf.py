from sqlalchemy import text

from models.usuario_acerto_cerf import UsuarioAcertoCerf


class UsuarioAcertoCERFRepository:
    def __init__(self, db):
        self.db = db

    def add_usuario_acerto_cerf(self, id_usuario: int, a1: int, a2: int, b1: int, b2: int, c1: int, c2: int):
        self.db.execute(text("""
            INSERT INTO usuario_acerto_cerf (id_usuario, "A1", "A2", "B1", "B2", "C1", "C2")
            VALUES (:id_usuario, :a1, :a2, :b1, :b2, :c1, :c2)
        """), {
            "id_usuario": id_usuario,
            "a1": a1,
            "a2": a2,
            "b1": b1,
            "b2": b2,
            "c1": c1,
            "c2": c2
        })
        self.db.commit()

    def update_usuario_acerto_cerf(self, id_usuario: int, a1: int, a2: int, b1: int, b2: int, c1: int, c2: int):
        self.db.execute(text("""
            UPDATE usuario_acerto_cerf
            SET "A1" = :a1, "A2" = :a2, "B1" = :b1, "B2" = :b2, "C1" = :c1, "C2" = :c2
            WHERE id_usuario = :id_usuario
        """), {
            "id_usuario": id_usuario,
            "a1": a1,
            "a2": a2,
            "b1": b1,
            "b2": b2,
            "c1": c1,
            "c2": c2
        })
        self.db.commit()


    def buscar_acertos_cerf_por_id_usuario(self, id_usuario: int):
        resultado = self.db.execute(text("""
            SELECT * FROM usuario_acerto_cerf
            WHERE id_usuario = :id_usuario
        """), {"id_usuario": id_usuario}).first()

        if resultado:
            return UsuarioAcertoCerf(
                id_usuario_acerto_cerf=resultado.id_usuario_acerto_cerf,
                id_usuario=resultado.id_usuario,
                A1=resultado.A1,
                A2=resultado.A2,
                B1=resultado.B1,
                B2=resultado.B2,
                C1=resultado.C1,
                C2=resultado.C2
            )
        return None