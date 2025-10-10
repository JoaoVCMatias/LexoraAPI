import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class SMTPService:
    msg = MIMEMultipart()

    def __init__(self, remetente: str, senha: str):
        self.remetente = remetente
        self.senha = senha
        self.msg['From'] = remetente

    def enviar_email(self, destinatario: str, assunto: str, corpo: str):
        self.msg.attach(MIMEText(corpo, 'html'))
        self.msg['Subject'] = assunto
        servidor = smtplib.SMTP('smtp.gmail.com', 587)
        try:
            servidor.starttls()  # Ativa criptografia
            print(self.remetente)
            print(self.senha)
            servidor.login(self.remetente, self.senha)
            servidor.sendmail(self.remetente, destinatario, self.msg.as_string())
            print("Email enviado com sucesso!")
        except Exception as e:
            print("Erro ao enviar email:", e)
        finally:
            servidor.quit()
    

