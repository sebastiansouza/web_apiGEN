# Use uma imagem oficial do Python como base
FROM python:3.12.2

# Define o diretório de trabalho
WORKDIR /app

# Cria um ambiente virtual
RUN python -m venv /opt/venv

# Ativa o ambiente virtual
ENV PATH="/opt/venv/bin:$PATH"

# Copia o arquivo de requerimentos e instala as dependências
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

# Copia o projeto
COPY . /app

