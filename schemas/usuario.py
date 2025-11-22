from pydantic import BaseModel, EmailStr, Field
from datetime import datetime as DateTime
from typing import List

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
    id_idioma: int
    id_experiencia_idioma: int 
    id_objetivo: int
    id_disponibilidade: int
    data_nascimento: DateTime

class UsuarioIdiomaDto(BaseModel):
    id_idioma: int
    id_experiencia_idioma: int 

class UsuarioResponse(BaseModel):
    email: EmailStr
    data_nascimento: DateTime
    experiencia_idioma_descricao: str
    objetivo_descricao: str
    disponibilidade_descricao: str

class QuestoesUsuarioResponse(BaseModel):
    id_questao: int
    descricao_questao: str
    json_opcao: str
    acerto: bool | None = None
    resposta: str | None = None

class UsuarioQuestaoReturn(BaseModel):
    id_conjunto_questao: int
    questoes: List[QuestoesUsuarioResponse] = Field(default_factory=list)

class RelatorioDesempenhoUsuarioResponse(BaseModel):
    questoes: List[UsuarioQuestaoReturn] = Field(default_factory=list)
    id_conjunto_questao: int
    tempo: str
    pontos: float
    porcentagem_acerto: float
    sequencia_acerto: int



