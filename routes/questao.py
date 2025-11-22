from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from services import DominioService
from services.questao import QuestaoService
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from services import UsuarioService, AutenticacaoService, ExperienciaIdiomaUsuarioService
from fastapi import Depends, HTTPException, status

router = APIRouter(prefix="/Questao", tags=["questao"])
security = HTTPBearer() 

@router.post("/ConjuntoQuestao")
def gerar_questoes(credentials: HTTPAuthorizationCredentials = Depends(security), db: Session = Depends(get_db)):
    token = credentials.credentials
    autenticacao_service = AutenticacaoService(db)
    validacao = autenticacao_service.validar_token(token)
    if isinstance(validacao, HTTPException):
        return validacao
    
    id_usuario = autenticacao_service.token_to_id_usuario(token)
    service = QuestaoService(db)
    result = service.gerar_questao_id(id_usuario)
    return result

@router.get("/ConjuntoQuestao")
def buscar_questoes(credentials: HTTPAuthorizationCredentials = Depends(security), db: Session = Depends(get_db)):
    token = credentials.credentials
    autenticacao_service = AutenticacaoService(db)
    validacao = autenticacao_service.validar_token(token)
    id_usuario = autenticacao_service.token_to_id_usuario(token)
    if isinstance(validacao, HTTPException):
        return validacao
    
    service = QuestaoService(db)
    result = service.buscar_questoes_usuario(id_usuario)
    return result

@router.post("/ResponderQuestao/{id_questao}/{alternativa}/{id_conjunto_questao}")
def responder_questao(id_questao: int, alternativa: int, id_conjunto   : int, credentials: HTTPAuthorizationCredentials = Depends(security), db: Session = Depends(get_db)):
    token = credentials.credentials
    autenticacao_service = AutenticacaoService(db)
    validacao = autenticacao_service.validar_token(token)
    
    if isinstance(validacao, HTTPException):
        return validacao
    
    id_usuario = autenticacao_service.token_to_id_usuario(token)
    service = QuestaoService(db)
    print(id_usuario)
    result = service.responder_questao(id_usuario, id_questao, alternativa, id_conjunto)
    return result
