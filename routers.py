from fastapi import APIRouter, HTTPException
from schemas import PredictInputSchema, PredictOutputSchema
from services import PredictionService

router = APIRouter(prefix="/api/v1", tags=["Obesity Prediction"])
try:
    # Inicializa o serviço carregando o pipeline serializado
    prediction_service = PredictionService()
except FileNotFoundError as e:
    # Se o script for inicializado sem o arquivo de modelo gerado
    prediction_service = None
    print("Aviso: Modelo serializado não encontrado. Por favor, treine e salve o modelo antes de subir a API.")

@router.post("/predict", response_model=PredictOutputSchema)
def predict_obesity(payload: PredictInputSchema):
    if prediction_service is None:
        raise HTTPException(status_code=503, detail="Serviço de predição indisponível devido à ausência do modelo.")

    try:
        prediction_result = prediction_service.predict(payload)
        return PredictOutputSchema(prediction=prediction_result, status="success")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro interno ao processar predição: {str(e)}")

@router.get("/health")
def health_check():
    return {"status": "ok", "model_loaded": prediction_service is not None}
