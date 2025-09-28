from pydantic import BaseModel

class UsuarioTokenCreate(BaseModel):
    id_usuario: int
    token: str