from pydantic import BaseModel, EmailStr
from datetime import datetime as DateTime

class UsuarioCreate(BaseModel):
    nome: str
    email: EmailStr
    senha: str

class UsuarioAutentication(BaseModel):
    email: EmailStr
    senha: str

class UsuarioResponse(BaseModel):
    nome: str
    email: EmailStr
    idioma_descricao: str
    experiencia_idioma_descricao: str
    objetivo_descricao: str
    disponibilidade_descricao: str
    data_nascimento: DateTime


class UsuarioInfosCreate(BaseModel):
    id_objetivo: int
    id_disponibilidade: int
    data_nascimento: DateTime

class UsuarioIdiomaDto(BaseModel):
    id_idioma: int
    id_experiencia_idioma: int 