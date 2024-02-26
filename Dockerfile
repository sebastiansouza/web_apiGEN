# Use uma imagem oficial do Python como base
FROM python:3.12.2

# Define o diretório de trabalho
WORKDIR /app

# Cria um ambiente virtual
RUN python -m venv /opt/venv

# Ativa o ambiente virtual
ENV PATH="/opt/venv/bin:$PATH"

# Instala o Poetry
RUN pip install poetry

# Copia o pyproject.toml e o poetry.lock para o contêiner
COPY pyproject.toml poetry.lock ./

# Usa o Poetry para instalar as dependências
RUN poetry config virtualenvs.create false && \
    poetry install --no-dev --no-interaction --no-ansi

# Copia o projeto
COPY . /app

# Comando de inicialização
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
