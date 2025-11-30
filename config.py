import os

# Ideal: buscar do ambiente, senão usa um fallback padrão
SECRET_KEY = os.getenv("SECRET_KEY", "54f7f97b394be356271a54321a9260da")
HORAS_TOKEN = 8
DATA_BASE = "postgresql://postgres:416158@localhost:5432/lexora"
EMAIL = "lexora.lab@gmail.com"
MAILTRAP_API_KEY = "7a6e0b52a76b6b93a8e04c8771941196"

#"postgresql://postgres:416158@localhost:5432/lexora"
#"postgresql://dpg-d3vndfre5dus73ahp2ag-a.oregon-postgres.render.com/dblexora_lqfv?user=lexora&password=N6HzxrTQzdOfTw9U8GQzIdxsLOSTlrH6"
