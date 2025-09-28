from fastapi import Depends
from sqlalchemy.orm import Session
from database import get_db
from models import sexo
from sqlalchemy.orm import Session

class DominioService:
    def __init__(self, db: Session):
        self.db = db
    
    def buscar_sexo(self):
        return self.db.query(sexo).all()