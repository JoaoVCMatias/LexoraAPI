from pydantic import BaseModel

class RelatorioEstatiticas(BaseModel):
    id_usuario: int
    dias_ativo: int
    atividades_feitas: int
    pontos_totais: int
    maior_sequencia: int
    ultima_sequencia: int

class RelatorioDataUsuario(BaseModel):
    data: str
    pontos: int | None = None

class RelatorioAtividadeUsuario(BaseModel):
    meta: int | None = None
    atividades_feitas: int | None = None