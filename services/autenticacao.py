import jwt
import datetime
from sqlalchemy.orm import Session
from config import SECRET_KEY
from schemas.usuario_token import UsuarioTokenCreate
from models.usuario_token import UsuarioToken
from fastapi import HTTPException
from fastapi.responses import JSONResponse

class AutenticacaoService:

    def __init__(self, db: Session):
        self.db = db

    def salvar_token(self, usuario_token: UsuarioTokenCreate):
        novo_token = UsuarioToken(id_usuario = usuario_token.id_usuario, token = usuario_token.token)
        self.db.add(novo_token)
        self.db.commit()
        self.db.refresh(novo_token)

    def buscar_token(self, id_usuario_login: int):
        usuario_token_cadastrado = self.db.query(UsuarioToken).filter(id_usuario = id_usuario_login).first()
        return usuario_token_cadastrado.token
    
    def delata_token(self, id_usuario: int):
        self.db.query(UsuarioToken).filter(UsuarioToken.id_usuario == id_usuario).delete()
    
    @staticmethod
    def gerar_token(id_usuario: int) -> str:
        # Tempo de expiração (8 horas)
        exp_time = datetime.datetime.utcnow() + datetime.timedelta(hours=8)

        payload = {
            "id_usuario": id_usuario,
            "exp": exp_time  # Data/hora de expiração
        }

        token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
        return token

    @staticmethod
    def validar_token(token: str):
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            return payload  # retorna os dados do token se válido
        except jwt.ExpiredSignatureError:
            raise HTTPException(
                status_code=401,
                detail="Token expirado!"
            )
        except jwt.InvalidTokenError:
            raise HTTPException(
                status_code=403,
                detail="Token inválido!"
            )

