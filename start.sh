#!/bin/bash

echo "Rodando migrations..."
alembic upgrade head   # aplica todas as migrations pendentes

echo "Iniciando aplicação..."
uvicorn main:app --host 0.0.0.0 --port $PORT