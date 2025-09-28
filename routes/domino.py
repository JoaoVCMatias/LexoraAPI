from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.usuario import UsuarioCreate
from database import get_db
from services import DominioService
import json

router = APIRouter(prefix="/Dominio", tags=["dominio"])

#@router.get("/", response_model=UsuarioResponse)

@router.get("/Sexo")
def buscar_sexo(db: Session = Depends(get_db)):
    service = DominioService(db)
    result = service.buscar_sexo()
    return json.dumps(result)
