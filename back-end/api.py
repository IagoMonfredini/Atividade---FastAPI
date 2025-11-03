from fastapi import FastAPI
from funcao import adicionar_produtos, listar_produtos, atualizar_produtos, buscar_produtos, deletar_produto

#Rodar o fastapi
# python -m uvicorn api:app --reload

#Testar api Fastapi
# /docs > Documentação Swagger
# /redoc > Documentação redoc

#Iniciar a fastapi
app = FastAPI(title="🛒Estoque de Produtos")

#GET = Pegar / Listar
#POST = Criar / Enviar
#PUT = Atualizar
#DELETE = Deletar 

@app.get("/")
def home(): 
    return {"mensagem": "Bem-vindo ao Estoque de Produtos"}

@app.post("/produtos")
def inserindo_produtos(nome: str, categoria: str, preco: float, quantidade: int):
    adicionar_produtos(nome, categoria, preco, quantidade)
    return {"mensagem": "Produto adicionado com sucesso!"}

@app.get("/produtos")
def exibir_produtos():
    produtos = listar_produtos()
    lista = []
    for linha in produtos:
        lista.append({
                "id": linha[0], 
                "nome": linha[1],
                "categoria": linha[2],
                "preco": linha[3],
                "quantidade": linha[4]
                })
    return {"Produto": lista}

