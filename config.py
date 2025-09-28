import os

# Ideal: buscar do ambiente, senão usa um fallback padrão
SECRET_KEY = os.getenv("SECRET_KEY", "54f7f97b394be356271a54321a9260da")
HORAS_TOKEN = 8
