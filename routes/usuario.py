from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
#from schemas import usuario as usuario_schema
from schemas.usuario import UsuarioCreate
from database import get_db
from models import Usuario
from datetime import date
#from app.schemas import UsuarioCreate, UsuarioResponse
from services import UsuarioService

router = APIRouter(prefix="/usuarios", tags=["usuarios"])

#@router.get("/", response_model=UsuarioResponse)

@router.post("/")
def criar_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    service = UsuarioService(db)
    result = service.Cadastrar_Usuario(usuario)
    return {result}
