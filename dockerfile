# Use uma imagem oficial de Python como base
FROM python:3.8-slim-buster

# Define o diretório de trabalho
WORKDIR /app

# Atualiza o pip
RUN pip install --upgrade pip

# Copia o arquivo de requerimentos e instala as dependências
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

# Copia o projeto
COPY . /app