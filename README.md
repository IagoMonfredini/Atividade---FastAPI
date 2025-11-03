# 🛒 Sistema de Gerenciamento de Estoque — FastAPI + PostgreSQL

Este projeto é uma aplicação **CRUD (Create, Read, Update, Delete)** desenvolvida em **Python**, utilizando o framework **FastAPI** e o banco de dados **PostgreSQL**.  
O objetivo é fornecer uma API moderna e eficiente para **gerenciar produtos em estoque**, com endpoints para cadastrar, listar, atualizar e deletar itens.

---

## ⚙️ Funcionalidades

✅ Cadastrar novos produtos no banco de dados  
✅ Listar todos os produtos cadastrados  
✅ Buscar produtos por ID  
✅ Atualizar preço e quantidade de um produto  
✅ Deletar produtos existentes  
✅ Conexão segura com o banco via variáveis de ambiente  
✅ Documentação automática da API via Swagger e ReDoc

---

## 🧩 Estrutura do Projeto

```bash
.
├── api.py           # Arquivo principal da API (endpoints e rotas)
├── conexao.py       # Responsável pela conexão com o PostgreSQL
├── funcao.py        # Funções de CRUD no banco de dados
├── .env             # Credenciais e parâmetros de conexão com o banco
├── .gitignore       # Arquivos e pastas ignorados pelo Git
└── requirements.txt # Dependências do projeto

Python 3.10+

FastAPI — Framework web rápido e moderno

PostgreSQL — Banco de dados relacional

psycopg2 — Biblioteca de conexão PostgreSQL

python-dotenv — Gerenciamento de variáveis de ambiente

Uvicorn — Servidor ASGI para rodar o FastAPI

git clone https://github.com/seu-usuario/estoque-fastapi.git
cd estoque-fastapi

Iago Monfredini - Coryright