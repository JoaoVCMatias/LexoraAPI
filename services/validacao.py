from sqlalchemy.orm import Session
from models import Usuario
from sqlalchemy.orm import Session
from sqlalchemy import exists

class ValidacaoService:
    
    def __init__(self, db: Session):
        self.db = db

    def Validacao_Email(self, email: str):
        return not self.db.query(
            exists().where(Usuario.email == email)
        ).scalar()