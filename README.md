# 📘 LexoraAPI

Projeto de API do Lexora

## 🚀 Como rodar o projeto

### 1. Crie e ative o ambiente virtual
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate.ps1     # Windows

#### 2. Instale as dependências
pip install -r requirements.txt

##### 3. Execute as migrations
configure o  database.py
alembic upgrade head

###### 4.Execute a aplicação
uvicorn main:app --reload

###### 5
.Acesse http://127.0.0.1:8000/docs



