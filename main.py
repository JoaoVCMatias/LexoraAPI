from fastapi import FastAPI
from routes.usuario import router as usuario_router
#from models import *
app = FastAPI(title="LexoraApi")

app.include_router(usuario_router)

#@app.get("/")
#def read_root():
#    return {"message": "API LeXota na VM!"}
#
#@app.get("/soma")
#def soma(a: int, b: int):
#    return {"resultado": a + b}
#