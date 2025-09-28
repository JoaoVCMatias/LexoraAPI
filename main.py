from fastapi import FastAPI
from routes.usuario import router as usuario_router

app = FastAPI(title="LexoraApi")

app.include_router(usuario_router)
