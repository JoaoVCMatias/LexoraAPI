from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from services import DominioService

router = APIRouter(prefix="/Dominio", tags=["dominio"])


@router.get("/Sexo")
def buscar_sexo(db: Session = Depends(get_db)):
    service = DominioService(db)
    result = service.buscar_sexo()
    return result

@router.get("/Idioma")
def buscar_idioma(db: Session = Depends(get_db)):
    service = DominioService(db)
    result = service.buscar_idioma()
    return result

@router.get("/ExperienciaIdioma")
def buscar_experiencia_idioma(db: Session = Depends(get_db)):
    service = DominioService(db)
    result = service.buscar_experiencia_idioma()
    return result

@router.get("/TipoQuestao")
def buscar_tipo_questao(db: Session = Depends(get_db)):
    service = DominioService(db)
    result = service.buscar_tipo_questao()
    return result

@router.get("/Objetivo")
def buscar_objetivo(db: Session = Depends(get_db)):
    service = DominioService(db)
    result = service.buscar_objetivo()
    return result

@router.get("/Disponibilidade")
def buscar_disponibilidade(db: Session = Depends(get_db)):
    service = DominioService(db)
    result = service.buscar_disponibilidade()
    return result

