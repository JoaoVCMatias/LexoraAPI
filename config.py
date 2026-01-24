import os 

SECRET_KEY = os.getenv("SECRET_KEY", "fallback_key")
HORAS_TOKEN = int(os.getenv("HORAS_TOKEN", 8))
DATA_BASE = os.getenv("DATA_BASE", "sqlite:///local.db")
EMAIL =  os.getenv("EMAIL", "lexora.lab@gmail.com")  
MAILTRAP_API_KEY = os.getenv("MAILTRAP_API_KEY", "")
TZ_BRASIL = pytz.timezone('America/Sao_Paulo')
