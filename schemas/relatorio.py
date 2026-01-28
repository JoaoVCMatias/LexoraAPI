from pydantic import BaseModel

class RelatorioEstatiticas(BaseModel):
    id_usuario: int | None = None
    dias_ativo: int | None = None
    atividades_feitas: int | None = None
    pontos_totais: int | None = None
    maior_sequencia: int | None = None
    ultima_sequencia: int | None = None

class RelatorioDataUsuario(BaseModel):
    data: str
    pontos: int | None = None

class RelatorioAtividadeUsuario(BaseModel):
    meta: int | None = None
    atividades_feitas: int | None = None