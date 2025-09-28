from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from services import ValidacaoService

router = APIRouter(prefix="/Validacao", tags=["validacao"])


@router.get("/Email")
def validar_email(email : str, db: Session = Depends(get_db)):
    service = ValidacaoService(db)
    result = service.Validacao_Email(email)
    return result
