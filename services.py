import joblib
import pandas as pd
import os
from schemas import PredictInputSchema

class PredictionService:
    def __init__(self, model_path: str = "models/obesity_rf_pipeline.joblib"):
        if not os.path.exists(model_path):
            raise FileNotFoundError(f"Modelo não encontrado no caminho: {model_path}")
        self.pipeline = joblib.load(model_path)

    def predict(self, input_data: PredictInputSchema) -> str:
        # Converter os dados de entrada do Pydantic em um DataFrame para o Pipeline
        data_dict = input_data.model_dump()
        df = pd.DataFrame([data_dict])

        # Executar a inferência através do Pipeline do Scikit-Learn
        prediction = self.pipeline.predict(df)[0]
        return prediction
