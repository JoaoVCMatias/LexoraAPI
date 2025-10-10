import os 

SECRET_KEY = os.getenv("SECRET_KEY", "fallback_key")
HORAS_TOKEN = int(os.getenv("HORAS_TOKEN", 8))
DATA_BASE = os.getenv("DATA_BASE", "sqlite:///local.db")
EMAIL =  os.getenv("EMAIL", "lexora.lab@gmail.com")  
PASS_WORD_EMAIL = os.getenv("PASS_WORD_EMAIL", "")  
