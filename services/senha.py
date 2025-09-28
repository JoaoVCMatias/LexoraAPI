import bcrypt

class SenhaService:
    
    def __init__(self):
        self.salt = bcrypt.gensalt()
        pass

    def ToHash(self, senha : str) -> bytes:
        return bcrypt.hashpw(senha.encode('utf-8'), self.salt)
    
    @staticmethod
    def Compare(senha : str, hash_senha_cadastrada : str):
        return bcrypt.checkpw(senha.encode('utf-8'), hash_senha_cadastrada)
        