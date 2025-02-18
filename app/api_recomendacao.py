from fastapi import FastAPI
import pickle
import pandas as pd
from surprise import SVD, Dataset, Reader

# Inicializar a API
app = FastAPI()

# Carregar o modelo treinado
modelo_path = "modelo_svd.pkl"
with open(modelo_path, "rb") as f:
    modelo = pickle.load(f)

# Carregar os dados usados no treinamento (para obter lista de produtos)
df = pd.read_csv("matriz_cliente_produto.csv")

# Criar lista de produtos únicos
produtos = df.columns[1:]  # Remove a coluna 'customer_unique_id'

@app.get("/")
def home():
    return {"message": "API de Recomendação de Produtos - FastAPI"}

@app.get("/predict")
def recomendar_produtos(customer_unique_id: str, n: int = 5):
    """
    Retorna os N produtos mais recomendados para um cliente.
    """
    recomendacoes = []
    
    for produto in produtos:
        predicao = modelo.predict(customer_unique_id, produto)
        recomendacoes.append((produto, predicao.est))
    
    # Ordenar recomendações
    recomendacoes.sort(key=lambda x: x[1], reverse=True)
    
    return {"customer_unique_id": customer_unique_id, "recomendacoes": recomendacoes[:n]}

# Rodar a API localmente
# Para rodar, use no terminal: uvicorn api_recomendacao:app --reload
