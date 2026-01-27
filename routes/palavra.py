
from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from requests import Session

from database import get_db
from services.autenticacao import AutenticacaoService
from services.palavra import PalavraService


router = APIRouter(prefix="/Palavra", tags=["palavra"])
security = HTTPBearer() 

# @router.get("/")
# def buscar_palavras(credentials: HTTPAuthorizationCredentials = Depends(security), db: Session = Depends(get_db)):
#     token = credentials.credentials
#     autenticacao_service = AutenticacaoService(db)
#     validacao = autenticacao_service.validar_token(token)
    
#     if isinstance(validacao, HTTPException):
#         return validacao
    
#     service = PalavraService(db)
#     result = service.buscar_todas_palavras()
#     return result

@router.get("/cerf/{nivel_cerf}")
def buscar_palavras_cerf(nivel_cerf: str, credentials: HTTPAuthorizationCredentials = Depends(security), db: Session = Depends(get_db)):
    token = credentials.credentials
    autenticacao_service = AutenticacaoService(db)
    validacao = autenticacao_service.validar_token(token)
    
    if isinstance(validacao, HTTPException):
        return validacao
    
    service = PalavraService(db)
    result = service.buscar_palavras_por_nivel_cerf(nivel_cerf)
    return result

@router.get("/id/{id_palavra}")
def buscar_palavra_id(id_palavra: int, credentials: HTTPAuthorizationCredentials = Depends(security), db: Session = Depends(get_db)):
    token = credentials.credentials
    autenticacao_service = AutenticacaoService(db)
    validacao = autenticacao_service.validar_token(token)
    
    if isinstance(validacao, HTTPException):
        return validacao
    
    service = PalavraService(db)
    result = service.buscar_palavra_por_id(id_palavra)
    return result

@router.get("/objetivo")
def buscar_palavras_objetivo_usuario(credentials: HTTPAuthorizationCredentials = Depends(security), db: Session = Depends(get_db)):
    token = credentials.credentials
    autenticacao_service = AutenticacaoService(db)
    validacao = autenticacao_service.validar_token(token)
    
    if isinstance(validacao, HTTPException):
        return validacao
    
    id_usuario = autenticacao_service.token_to_id_usuario(token)
    service = PalavraService(db)
    result = service.busca_palavras_por_objetivo_usuario(id_usuario)
    return result

@router.get("/descricao/{palavra}")
def buscar_palavra_por_descricao(palavra: str, credentials: HTTPAuthorizationCredentials = Depends(security), db: Session = Depends(get_db)):
    token = credentials.credentials
    autenticacao_service = AutenticacaoService(db)
    validacao = autenticacao_service.validar_token(token)
    
    if isinstance(validacao, HTTPException):
        return validacao

    service = PalavraService(db)
    result = service.buscar_palavras_por_descricao(palavra)
    return result