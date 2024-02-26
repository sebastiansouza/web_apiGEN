# API Web com Deploy no Render

## Descrição do Projeto

Este projeto consiste na criação de uma API Web utilizando a linguagem Python e o framework FastAPI. A API permite realizar operações básicas de um CRUD (Create, Read, Update, Delete) para três entidades principais: usuários, temas e postagens. Além disso, a aplicação é documentada utilizando o Swagger/OpenAPI para facilitar os testes e a compreensão das rotas disponíveis. Este projeto é um desafio do curso re/start da Generation em parceria com a AWS.


## Arquitetura do Projeto

O projeto segue uma arquitetura MVC (Model-View-Controller), com as seguintes camadas:

- **Models**: Definições das tabelas do banco de dados utilizando SQLAlchemy.
- **Routes**: Rotas da API utilizando o framework FastAPI.
- **Schemas**: Modelos de dados utilizando Pydantic para validação e serialização.
- **CRUD**: Operações de criação, leitura, atualização e exclusão dos dados no banco de dados.
- **Database**: Configuração da conexão com o banco de dados.

## Dependências do Projeto

- Python: 3.12.2
- FastAPI: 0.110.0
- SQLAlchemy: 2.0.27
- Pydantic: 2.6.2
- Poetry: 1.1.12
- Uvicorn: 0.27.1

# Acesse a documentação 

O projeto foi feito o deploy usando o render. Com o dockerfile que gera uma esteira de CI/CD. Você pode conferir a documentação e entender melhor o CRUD e a API abaixo:

## [render/docs](https://web-apigen.onrender.com/docs)

 
## Contribuição

Contribuições são bem-vindas! Se você tiver alguma sugestão, correção de bug ou novos recursos, fique à vontade para abrir uma issue ou enviar um pull request.

