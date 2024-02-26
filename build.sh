#!/usr/bin/env bash
# exit on error
set -o errexit

# Instala as dependências do projeto
poetry install

# Inicia o servidor FastAPI
uvicorn main:app --host  0.0.0.0 --port  8000
