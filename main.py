from fastapi import FastAPI
from routes import usuario_router, dominio_router, validacao_router, questao_router, relatorio_router, palavra_router

app = FastAPI(title="LexoraApi")

app.include_router(usuario_router)
app.include_router(dominio_router)
app.include_router(validacao_router)
app.include_router(questao_router)
app.include_router(relatorio_router)
app.include_router(palavra_router)


