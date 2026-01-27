from typing import List
from pydantic import BaseModel, Field


class PalavraCreate(BaseModel):
    id_palavra: int
    descricao_palavra: str
    descricao_palavra_traducao: str | None = None
    CEFR: str

class ObjetivoPalavras(BaseModel):
    id_objetivo_usuario: int
    id_objetivo: int
    descricao_objetivo: str
    palavras: List[PalavraCreate] = Field(default_factory=list)