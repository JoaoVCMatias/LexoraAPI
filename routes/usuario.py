from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
#from schemas import usuario as usuario_schema
from schemas.usuario import UsuarioCreate
from database import get_db
from models import Usuario
from datetime import date
#from app.schemas import UsuarioCreate, UsuarioResponse

router = APIRouter(prefix="/usuarios", tags=["usuarios"])

#@router.get("/", response_model=UsuarioResponse)

@router.post("/")
def criar_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    data_atual = date.today()
    novo_usuario = Usuario(nome = usuario.nome, email = usuario.email, senha = usuario.senha, cadastro_completo = 0, data_ultimo_acesso = data_atual, data_criacao = data_atual)
    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)
    return {1}
