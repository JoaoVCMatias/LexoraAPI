from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.usuario import UsuarioCreate
from database import get_db
from services import UsuarioService
import json

router = APIRouter(prefix="/usuarios", tags=["usuarios"])

#@router.get("/", response_model=UsuarioResponse)

@router.post("/")
def criar_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    service = UsuarioService(db)
    result = service.Cadastrar_Usuario(usuario)
    return json.dumps(result)
