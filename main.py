from fastapi import FastAPI
from contextlib import asynccontextmanager
import joblib
import os
from routers import router as api_router

# Definição do Lifespan Manager
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Código executado durante a INICIALIZAÇÃO da aplicação
    model_path = "models/obesity_rf_pipeline.joblib"
    print(f"[Lifespan] Inicializando API e carregando modelo de {model_path} na RAM...")

    if os.path.exists(model_path):
        # Carrega uma única vez na RAM e associa ao estado global do app
        app.state.model_pipeline = joblib.load(model_path)
        print("[Lifespan] Modelo carregado com sucesso na memória!")
    else:
        print("[Lifespan] CRÍTICO: Arquivo de modelo serializado não encontrado!")
        app.state.model_pipeline = None

    yield # A aplicação fica ativa respondendo requisições HTTP

    # Código executado quando a aplicação é ENCERRADA
    print("[Lifespan] Encerrando API e limpando recursos...")
    if hasattr(app.state, "model_pipeline"):
        del app.state.model_pipeline

# Inicialização do FastAPI com lifespan
app = FastAPI(
    title="API de Classificação de Níveis de Obesidade",
    description="API otimizada com ciclo de vida (lifespan) garantindo leitura única de modelo na RAM.",
    version="1.1.0",
    lifespan=lifespan
)

app.include_router(api_router)

@app.get("/")
def root():
    return {
        "message": "API para Predição e Classificação de Obesidade ativa.",
        "documentation": "/docs"
    }
