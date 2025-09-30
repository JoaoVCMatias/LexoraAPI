from fastapi import APIRouter, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from schemas.usuario import UsuarioCreate, UsuarioAutentication, UsuarioInfosCreate
from database import get_db
from services import UsuarioService
from services import AutenticacaoService
import json

router = APIRouter(prefix="/usuarios", tags=["usuarios"])
security = HTTPBearer() 
#@router.get("/", response_model=UsuarioResponse)

@router.post("/")
def criar_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    service = UsuarioService(db)
    result = service.cadastrar_usuario(usuario)
    return json.dumps(result)

@router.post("/Login")
def login_usuario(usuario: UsuarioAutentication, db: Session = Depends(get_db)):
    service = UsuarioService(db)
    result = service.validar_autenticacao(usuario)
    return json.dumps(result)

@router.post("/Logout")
def logout_usuario(credentials: HTTPAuthorizationCredentials = Depends(security),db: Session = Depends(get_db)):
    token = credentials.credentials
    service = AutenticacaoService(db)
    service.delata_token_por_token(token)

    return json.dumps(1)

@router.put("/UsuarioInformacao")
def alterar_usuario_informacao(usuario_info_change: UsuarioInfosCreate, credentials: HTTPAuthorizationCredentials = Depends(security), db: Session = Depends(get_db)):
    token = credentials.credentials
    id_usuario = AutenticacaoService.token_to_id_usuario(token)
    service = UsuarioService(db)
    service.alterar_usuario_informacao(id_usuario, usuario_info_change)
    return json.dumps(1)
