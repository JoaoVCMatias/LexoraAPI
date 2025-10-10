
class EmailHtml:
    
    @staticmethod
    def envio_codigo_verificacao(codigo: str):
        return f"""
        <!DOCTYPE html>
        <html lang="pt-BR">
        <head>
            <meta charset="UTF-8">
            <title>Código de Verificação</title>
            <style>
                body {{ font-family: Arial, sans-serif; background-color: #f4f4f4; margin: 0; padding: 0; }}
                .container {{ background-color: #ffffff; max-width: 600px; margin: 50px auto; border-radius: 8px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); overflow: hidden; }}
                .header {{ background-color: #007BFF; color: white; padding: 20px; text-align: center; }}
                .header h1 {{ margin: 0; font-size: 24px; }}
                .content {{ padding: 30px 20px; text-align: center; color: #333333; }}
                .code {{ font-size: 28px; font-weight: bold; color: #007BFF; background-color: #f0f8ff; display: inline-block; padding: 15px 25px; border-radius: 6px; margin: 20px 0; letter-spacing: 2px; }}
                .footer {{ padding: 15px 20px; text-align: center; font-size: 12px; color: #777777; background-color: #f9f9f9; }}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="header"><h1>Verificação de Email</h1></div>
                <div class="content">
                    <p>Olá,</p>
                    <p>Seu código de verificação é:</p>
                    <div class="code">{codigo}</div>
                    <p>Insira este código no aplicativo para confirmar seu endereço de e-mail.</p>
                    <p>Se você não solicitou este código, pode ignorar este email.</p>
                </div>
                <!-- <div class="footer">&copy; 2025 Sua Empresa. Todos os direitos reservados.</div> -->
            </div>
        </body>
        </html>
        """