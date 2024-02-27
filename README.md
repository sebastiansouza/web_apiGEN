# API Web com Deploy no Render

## Descrição do Projeto

Este projeto consiste na criação de uma API Web utilizando Python e o framework FastAPI. A API possibilita operações básicas de CRUD (Create, Read, Update, Delete) para três entidades principais: usuários, postagens e temas. A aplicação é documentada utilizando Swagger/OpenAPI para facilitar os testes e a compreensão das rotas disponíveis. Desenvolvido como parte do desafio do curso re/start da Generation em parceria com a AWS.

## Arquitetura do Projeto

O projeto segue uma arquitetura MVC (Model-View-Controller), com as seguintes camadas:

- **Models**: Define a estrutura das tabelas do banco de dados utilizando SQLAlchemy.
- **Routes**: Define as rotas da API utilizando o framework FastAPI.
- **Schemas**: Define os modelos de dados utilizando Pydantic para validação e serialização.
- **CRUD**: Implementa operações de criação, leitura, atualização e exclusão dos dados no banco de dados.
- **Database**: Configura a conexão com o banco de dados.

## Entidades e Relacionamentos das Tabelas

### Usuário
- **Campos**:
  - `id`: Identificador único do usuário.
  - `nome`: Nome do usuário.
  - `email`: Endereço de e-mail do usuário.
  - `foto`: URL da foto do usuário.
- **Relacionamentos**:
  - Uma postagem pertence a um único usuário (`N <-> 1`).

### Postagem
- **Campos**:
  - `id`: Identificador único da postagem.
  - `título`: Título da postagem.
  - `texto`: Texto da postagem.
  - `data`: Data de criação da postagem.
  - `usuario_id`: Chave estrangeira referenciando o usuário que criou a postagem.
  - `tema_id`: Chave estrangeira referenciando o tema da postagem.
- **Relacionamentos**:
  - Uma postagem pertence a um único usuário (`N <-> 1`).
  - Uma postagem pertence a um único tema (`N <-> 1`).

### Tema
- **Campos**:
  - `id`: Identificador único do tema.
  - `descrição`: Descrição do tema.
- **Relacionamentos**:
  - Um tema pode ter várias postagens (`1 <-> N`).

  
## Dependências do Projeto

- Python: 3.12.2
- FastAPI: 0.110.0
- SQLAlchemy: 2.0.27
- Pydantic: 2.6.2
- Poetry: 1.1.12
- Uvicorn: 0.27.1



### Diagrama de Arquitetura

```
APIWEB-PY/
│
├── app/
│   ├── __init__.py
│   ├── database.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user_models.py
│   │   ├── theme_models.py
│   │   └── post_models.py
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── user_routes.py
│   │   ├── theme_routes.py
│   │   └── post_routes.py
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── user_schema.py
│   │   ├── theme_schema.py
│   │   └── post_schema.py
│   └── crud/
│       ├── __init__.py
│       ├── user_crud.py
│       ├── theme_crud.py
│       └── post_crud.py
│
│
├── poetry-api
│   │
│   └── __init__.py
├── tests
│   │
│   └── __init__.py
├── .gitignore
│
├── build.sh
│
├── poetry.lock
│
├── pyproject.toml
│
├── README.md
│
├── render.yaml
│
├── Dockerfile
│
├── docker-compose.yaml
│
├── requirements.txt
│
├── .env
│
└── main.py
```

# Acesse a documentação 

O projeto foi feito o deploy usando o render. Com o dockerfile que gera uma esteira de CI/CD. Você pode conferir a documentação e entender melhor o CRUD e a API abaixo:

## [render/docs](https://web-apigen.onrender.com/docs)

 
## Contribuição

Contribuições são bem-vindas! Se você tiver alguma sugestão, correção de bug ou novos recursos, fique à vontade para abrir uma issue ou enviar um pull request.
