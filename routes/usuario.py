from fastapi import APIRouter, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from schemas.usuario import UsuarioCreate, UsuarioAutentication, UsuarioInfosCreate
from database import get_db
from services import UsuarioService, AutenticacaoService, ExperienciaIdiomaUsuarioService
import json
from fastapi import Depends, HTTPException, status

router = APIRouter(prefix="/usuarios", tags=["usuarios"])
security = HTTPBearer() 
#@router.get("/", response_model=UsuarioResponse)

@router.post("/")
def criar_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    service = UsuarioService(db)
    result = service.cadastrar_usuario(usuario)
    return result

@router.get("/Usuario")
def pesquisar_usuario_logado(credentials: HTTPAuthorizationCredentials = Depends(security), db: Session = Depends(get_db)):
    service = UsuarioService(db)
    token = credentials.credentials
    autenticacao_service = AutenticacaoService(db)
    validacao = autenticacao_service.validar_token(token)
    if isinstance(validacao, HTTPException):
        return validacao
    id_usuario = autenticacao_service.token_to_id_usuario(token)
    result = service.pesquisar_usuario_logado(id_usuario)
    return result

@router.post("/Login")
def login_usuario(usuario: UsuarioAutentication, db: Session = Depends(get_db)):
    service = UsuarioService(db)
    result = service.validar_autenticacao(usuario)
    return result

@router.post("/Logout")
def logout_usuario(credentials: HTTPAuthorizationCredentials = Depends(security),db: Session = Depends(get_db)):
    token = credentials.credentials
    service = AutenticacaoService(db)
    service.delata_token_por_token(token)

    return json.dumps(1)

@router.post("/UsuarioInformacao")
def alterar_usuario_informacao(usuario_info_change: UsuarioInfosCreate, credentials: HTTPAuthorizationCredentials = Depends(security), db: Session = Depends(get_db)):
    token = credentials.credentials
    autenticacao_service = AutenticacaoService(db)
    validacao = autenticacao_service.validar_token(token)
    if isinstance(validacao, HTTPException):
        return validacao
    id_usuario = AutenticacaoService.token_to_id_usuario(token)
    service = UsuarioService(db)
    service.alterar_usuario_informacao(id_usuario, usuario_info_change)
    return json.dumps(1)

@router.get("/UsuarioInformacao")
def pesquisar_usuario_informacao(credentials: HTTPAuthorizationCredentials = Depends(security), db: Session = Depends(get_db)):
    token = credentials.credentials
    autenticacao_service = AutenticacaoService(db)
    validacao = autenticacao_service.validar_token(token)
    if isinstance(validacao, HTTPException):
        return validacao
    id_usuario = autenticacao_service.token_to_id_usuario(token)
    service = UsuarioService(db)
    dados = service.pesquisar_usuario_info(id_usuario)
    return dados

@router.post("/Usuario/IdiomaExperiencia")
def cadastrar_idioma_experiencia(id_idioma: int, id_experiencia_idioma: int, credentials: HTTPAuthorizationCredentials = Depends(security), db: Session = Depends(get_db)):
    token = credentials.credentials
    autenticacao_service = AutenticacaoService(db)
    validacao = autenticacao_service.validar_token(token)
    if isinstance(validacao, HTTPException):
        return validacao
    id_usuario = AutenticacaoService.token_to_id_usuario(token)
    service = ExperienciaIdiomaUsuarioService(db)
    service.cadastrar_experiencia_idioma_usuario(id_idioma, id_usuario, id_experiencia_idioma)
    return json.dumps(1)

@router.put("/Usuario/IdiomaExperiencia")
def alterar_idioma_experiencia(id_experiencia_idioma_usuario: int, id_experiencia_idioma: int, credentials: HTTPAuthorizationCredentials = Depends(security), db: Session = Depends(get_db)):
    token = credentials.credentials
    autenticacao_service = AutenticacaoService(db)
    validacao = autenticacao_service.validar_token(token)
    if isinstance(validacao, HTTPException):
        return validacao
    service = ExperienciaIdiomaUsuarioService(db)
    service.alterar_experiencia_idioma_usuario(id_experiencia_idioma_usuario, id_usuario, id_experiencia_idioma)
    return json.dumps(1)
