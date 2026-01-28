from sqlalchemy.orm import Session
from models import Usuario, ExperienciaIdiomaUsuario
from schemas.usuario import UsuarioInfosCreate 
from sqlalchemy import text
from dto.usuario_info_dto import UsuarioInfoDto
from dto.usuario_experiencia_idioma_dto import UsuarioExperienciaIdiomaDto
from dto.usuario_objetivo_dto import UsuarioObjetivoDto

class UsuarioRepository:
    def __init__(self, db: Session):
        self.db = db
    
    def buscar_usuario_por_id(self, id_usuario: int):
        usuario = self.db.query(Usuario).filter(Usuario.id_usuario == id_usuario).first()
        return usuario
    
    def buscar_usuario_por_email(self, email: str):
        usuario = self.db.query(Usuario).filter(Usuario.email == email).first()
        return usuario
    
    def buscar_dados_usuario(self, id_usuario: int)-> UsuarioInfoDto | None: 
        row = self.db.execute(text("""
            SELECT u.id_usuario, u.nome, u.data_nascimento, u.email, d.id_disponibilidade, d.descricao_disponibilidade
            FROM usuario u
            LEFT JOIN disponibilidade d ON d.id_disponibilidade = u.id_disponibilidade
            WHERE u.id_usuario = :id
        """), {"id": id_usuario}).first()

        if row:
            return UsuarioInfoDto(
                id_usuario=row.id_usuario,
                nome=row.nome,
                data_nascimento=row.data_nascimento,
                email=row.email,
                id_disponibilidade=row.id_disponibilidade,
                descricao_disponibilidade=row.descricao_disponibilidade
            )
        return None
    
    def buscar_idioma_usuario(self, id_usuario)-> UsuarioExperienciaIdiomaDto | None:
        row = self.db.execute(text(""" 
            select eiu.id_experiencia_idioma_usuario, eiu.id_idioma, i.descricao_idioma , ei.id_experiencia_idioma, ei.descricao_experiencia_idioma   
            from experiencia_idioma_usuario eiu 
            left join experiencia_idioma ei 
	            on ei.id_experiencia_idioma  = eiu.id_experiencia_idioma 
            left join idioma i 
	        on i.id_idioma = eiu.id_idioma 
            left join usuario u 
	        on u.id_usuario  = eiu.id_usuario
            where u.id_usuario = :id"""), {"id": id_usuario}).first()
        if row:
            return UsuarioExperienciaIdiomaDto(
                id_experiencia_idioma_usuario=row.id_experiencia_idioma_usuario,
                id_idioma=row.id_idioma,
                descricao_idioma=row.descricao_idioma,
                id_experiencia_idioma=row.id_experiencia_idioma,
                descricao_experiencia_idioma=row.descricao_experiencia_idioma
            )
        return None
  
    
    def buscar_objetivos_usuario(self, id_usuario) -> UsuarioObjetivoDto | None: 
        row = self.db.execute(text("""
            select ou.id_objetivo_usuario, o.id_objetivo , o.descricao_objetivo
            from objetivo_usuario ou 
            inner join objetivo o  
            	on o.id_objetivo  = ou.id_objetivo 
            inner join usuario u 
            	on U.id_usuario  = ou.id_usuario 
            where  U.id_usuario  = :id
            and ou.ativo = true 
            and ou.data_exclusao is null
        """), {"id": id_usuario}).first()

        if row:
            return UsuarioObjetivoDto(
                id_objetivo_usuario=row.id_objetivo_usuario,
                id_objetivo=row.id_objetivo,
                descricao_objetivo=row.descricao_objetivo,
            )
        return None
    def inserir_usuario(self, novo_usuario: Usuario):
        self.db.add(novo_usuario)
        self.db.commit()
        self.db.refresh(novo_usuario)
        print("Log: Usuario cadastrado")

    def inseir_informacoes_usuario(self, id_usuario: int, usuario_alteracao: UsuarioInfosCreate):
        usuario_cadastrado = self.db.query(Usuario).filter(Usuario.id_usuario == id_usuario).first()
        usuario_cadastrado.id_idioma_materno = 1
        usuario_cadastrado.id_disponibilidade = usuario_alteracao.id_disponibilidade
        usuario_cadastrado.data_nascimento = usuario_alteracao.data_nascimento
        self.db.commit()
    
    def concluir_cadastro(self, id_usuario):
        usuario_cadastrado = self.db.query(Usuario).filter(Usuario.id_usuario == id_usuario).first()
        usuario_cadastrado.cadastro_completo = True
        self.db.commit()    

