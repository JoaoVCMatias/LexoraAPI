from pydantic import BaseModel, EmailStr

class UsuarioCreate(BaseModel):
    nome: str
    email: EmailStr
    senha: str

class UsuarioAutentication(BaseModel):
    email: EmailStr
    senha: str

class UsuarioResponse(BaseModel):
    pass