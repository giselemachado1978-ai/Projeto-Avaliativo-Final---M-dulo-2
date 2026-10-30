from fastapi import APIRouter, HTTPException, Request
from schemas import PredictInputSchema, PredictOutputSchema
import pandas as pd

router = APIRouter(prefix="/api/v1", tags=["Obesity Prediction"])

@router.post("/predict", response_model=PredictOutputSchema)
def predict_obesity(payload: PredictInputSchema, request: Request):
    # Obtendo o pipeline que foi pré-carregado no estado global da aplicação durante a inicialização (Lifespan)
    model_pipeline = getattr(request.app.state, "model_pipeline", None)

    if model_pipeline is None:
        raise HTTPException(
            status_code=503,
            detail="O modelo de predição não foi carregado corretamente na memória RAM da aplicação."
        )

    try:
        # Conversão direta do input Pydantic para DataFrame
        data_dict = payload.model_dump()
        df = pd.DataFrame([data_dict])
        prediction_result = model_pipeline.predict(df)[0]

        return PredictOutputSchema(prediction=prediction_result, status="success")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro interno na inferência: {str(e)}")

@router.get("/health")
def health_check(request: Request):
    model_loaded = getattr(request.app.state, "model_pipeline", None) is not None
    return {"status": "ok", "model_loaded": model_loaded}
