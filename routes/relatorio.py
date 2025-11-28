from fastapi import APIRouter, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from schemas.usuario import UsuarioCreate, UsuarioAutentication, UsuarioInfosCreate
from database import get_db
from services import UsuarioService, RelatorioService, AutenticacaoService
import json
from fastapi import Depends, HTTPException, status

router = APIRouter(prefix="/relatorio", tags=["relatorios"])
security = HTTPBearer() 

@router.get("/EstatisticaUsuario")
def pesquisar_estatistica_usuario(credentials: HTTPAuthorizationCredentials = Depends(security), db: Session = Depends(get_db)):
    service = UsuarioService(db)
    token = credentials.credentials
    autenticacao_service = AutenticacaoService(db)
    service = RelatorioService(db)
    validacao = autenticacao_service.validar_token(token)
    if isinstance(validacao, HTTPException):
        return validacao
    id_usuario = autenticacao_service.token_to_id_usuario(token)
    result = service.buscar_relatorio_estatistica_usuario(id_usuario)
    return result

@router.get("/DataUsuario")
def relatorio_data_usuario(credentials: HTTPAuthorizationCredentials = Depends(security), db: Session = Depends(get_db)):
    service = UsuarioService(db)
    token = credentials.credentials
    autenticacao_service = AutenticacaoService(db)
    service = RelatorioService(db)
    validacao = autenticacao_service.validar_token(token)
    if isinstance(validacao, HTTPException):
        return validacao
    id_usuario = autenticacao_service.token_to_id_usuario(token)
    result = service.buscar_relatorio_data_usuario(id_usuario)
    return result

@router.get("/AtividadeUsuario")
def relatorio_atividade_usuario(credentials: HTTPAuthorizationCredentials = Depends(security), db: Session = Depends(get_db)):
        service = UsuarioService(db)
        token = credentials.credentials
        autenticacao_service = AutenticacaoService(db)
        service = RelatorioService(db)
        validacao = autenticacao_service.validar_token(token)
        if isinstance(validacao, HTTPException):
            return validacao
        id_usuario = autenticacao_service.token_to_id_usuario(token)
        result = service.buscar_metas_usuario(id_usuario)
        return result