from fastapi import  HTTPException
from repository.relatorio import RelatorioRepository
from sqlalchemy.orm import Session
from datetime import date
from datetime import datetime
from repository.usuario import UsuarioRepository
import json

class RelatorioService:

    def __init__(self, db: Session):
        self.db = db

    def buscar_relatorio_estatistica_usuario(self, id_usuario: int):
        relatorio = RelatorioRepository.buscar_relatorio_estatistica_usuario(self, id_usuario)
        return relatorio
    
    def buscar_relatorio_data_usuario(self, id_usuario: int):
        relatorio = RelatorioRepository.buscar_relatorio_data_usuario(self, id_usuario)
        return relatorio
    
    def buscar_metas_usuario(self, id_usuario: int):
        relatorio = RelatorioRepository.buscar_metas_usuario(self, id_usuario)
        return relatorio