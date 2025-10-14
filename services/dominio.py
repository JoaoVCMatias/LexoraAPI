from sqlalchemy.orm import Session
from models import Sexo, Disponibilidade, ExperienciaIdioma, Idioma, Objetivo, TipoQuestao, Palavra
from sqlalchemy.orm import Session

class DominioService:
    def __init__(self, db: Session):
        self.db = db

    def buscar_sexo(self):
        return self.db.query(Sexo).all()
    
    def buscar_experiencia_idioma(self):
        return self.db.query(ExperienciaIdioma).all()
    
    def buscar_idioma(self):
        return self.db.query(Idioma).all()
    
    def buscar_disponibilidade(self):
        return self.db.query(Disponibilidade).all()
    
    def buscar_objetivo(self):
        return self.db.query(Objetivo).all()
    
    def buscar_tipo_questao(self):
        return self.db.query(TipoQuestao).all()
    
    def buscar_palavra(self):
        return self.db.query(Palavra).all()