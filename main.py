from fastapi import FastAPI
from routers import router as api_router

app = FastAPI(
    title="API de Classificação de Níveis de Obesidade",
    description="API modular construída para o projeto prático final, focada na predição de níveis de obesidade.",
    version="1.0.0"
)

# Inclui as rotas desenvolvidas de forma modular
app.include_router(api_router)

@app.get("/")
def root():
    return {
        "message": "API para Predição e Classificação de Obesidade ativa.",
        "documentation": "/docs"
    }
