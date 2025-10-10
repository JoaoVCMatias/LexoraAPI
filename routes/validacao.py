from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from services import ValidacaoService, EmailService, UsuarioService, AutenticacaoService
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

router = APIRouter(prefix="/Validacao", tags=["validacao"])
security = HTTPBearer() 

@router.get("/Email")
def validar_email(email : str, db: Session = Depends(get_db)):
    service = ValidacaoService(db)
    result = service.Validacao_Email(email)
    return result

@router.post("/EnviarCodigoVerificacaoEmail")
def enviar_codigo_email(credentials: HTTPAuthorizationCredentials = Depends(security), db: Session = Depends(get_db)):
    service = UsuarioService(db)
    token = credentials.credentials
    autenticacao_service = AutenticacaoService(db)
    validacao = autenticacao_service.validar_token(token)
    if isinstance(validacao, HTTPException):
        return validacao
    id_usuario = AutenticacaoService.token_to_id_usuario(token)
    email_service = EmailService(db)
    result = email_service.enviar_codigo_email(id_usuario)
    return result

@router.post("/CodigoVerificacaoEmail/CodigoValidacao")
def validar_codigo_email(codigo: int,credentials: HTTPAuthorizationCredentials = Depends(security), db: Session = Depends(get_db)):
    token = credentials.credentials
    autenticacao_service = AutenticacaoService(db)
    validacao = autenticacao_service.validar_token(token)
    if isinstance(validacao, HTTPException):
        return validacao
    id_usuario = AutenticacaoService.token_to_id_usuario(token)
    print("Criando Service")
    email_service = EmailService(db)
    result = email_service.validar_email(id_usuario, codigo)
    return result
