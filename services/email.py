from sqlalchemy.orm import Session
from models import EmailConfirmacao, Usuario
import random
from .SMTP import SMTPService
from html import EmailHtml
from config import PASS_WORD_EMAIL, EMAIL

class EmailService:
    
    def __init__(self, db: Session):
        self.db = db
    
    def deletar_codigo_email(self, id_email_confirmacao: int):
        self.db.query(EmailConfirmacao).filter(EmailConfirmacao.id_email_confirmacao == id_email_confirmacao).delete(synchronize_session='fetch')
        self.db.commit()
        pass

    def enviar_email(self, id_usuario: int):
        usuario = self.db.query(Usuario).filter(Usuario.id_usuario == id_usuario).first()
        codigo = random.randint(100000, 999999)
        mensagem = EmailHtml.envio_codigo_verificacao(str(codigo))
        smtp_service = SMTPService(EMAIL, PASS_WORD_EMAIL)
        smtp_service.enviar_email(usuario.email, "Código de acesso", mensagem)
        email = EmailConfirmacao(id_usuario = id_usuario, codigo = codigo)
        self.db.add(email)
        self.db.commit()
        self.db.refresh(email)
        return 1 


    def enviar_codigo_email(self, id_usuario: int):
        email_confirmacao = self.db.query(EmailConfirmacao).filter(EmailConfirmacao.id_usuario == id_usuario).first()
        if email_confirmacao is not None:
            self.deletar_codigo_email(email_confirmacao.id_email_confirmacao)
            
        self.enviar_email(id_usuario)

    def validar_email(self, id_usuario: int, codigo: int):
        usuario = self.db.query(Usuario).filter(Usuario.id_usuario == id_usuario).first()
        
        if(usuario.cadastro_completo == True):
            print("cadastro já completo")
            return 1
        print(codigo)
        usuario_codigo = self.db.query(EmailConfirmacao).filter(EmailConfirmacao.id_usuario == id_usuario).first()
        if(usuario_codigo.codigo != codigo):
            return 0
        usuario.cadastro_completo = 1
        self.db.commit()
        self.db.refresh(usuario)
        return 1