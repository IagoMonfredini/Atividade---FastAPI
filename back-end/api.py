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

