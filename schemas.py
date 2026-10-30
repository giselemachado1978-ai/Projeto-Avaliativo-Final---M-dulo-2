from pydantic import BaseModel, Field
from typing import Optional

class PredictInputSchema(BaseModel):
    Gender: str = Field(..., description="Gênero do indivíduo (Female ou Male)", example="Female")
    Age: float = Field(..., description="Idade em anos", ge=0, le=120, example=45.0)
    Height: float = Field(..., description="Altura em metros", ge=0.5, le=2.5, example=1.65)
    Weight: float = Field(..., description="Peso em quilogramas", ge=10.0, le=300.0, example=68.0)
    family_history_with_overweight: str = Field(..., description="Histórico familiar de sobrepeso (yes ou no)", example="yes")
    FAVC: str = Field(..., description="Consumo frequente de alimentos de alto teor calórico (yes ou no)", example="no")
    FCVC: float = Field(..., description="Frequência de consumo de vegetais (normalmente de 1 a 3)", ge=1.0, le=3.0, example=2.0)
    NCP: float = Field(..., description="Número de refeições principais por dia", ge=1.0, le=4.0, example=3.0)
    CAEC: str = Field(..., description="Consumo de comida entre as refeições (no, Sometimes, Frequently, Always)", example="Sometimes")
    SMOKE: str = Field(..., description="Se o paciente fuma (yes ou no)", example="no")
    CH2O: float = Field(..., description="Consumo diário de água em litros", ge=1.0, le=3.0, example=2.0)
    SCC: str = Field(..., description="Monitoramento do consumo de calorias (yes ou no)", example="no")
    FAF: float = Field(..., description="Frequência de atividade física por semana (0 a 3)", ge=0.0, le=3.0, example=1.0)
    TUE: float = Field(..., description="Tempo de uso de dispositivos eletrônicos por dia (0 a 2)", ge=0.0, le=2.0, example=1.0)
    CALC: str = Field(..., description="Consumo de álcool (no, Sometimes, Frequently, Always)", example="Sometimes")
    MTRANS: str = Field(..., description="Meio de transporte utilizado", example="Public_Transportation")

class PredictOutputSchema(BaseModel):
    prediction: str = Field(..., description="Classe predita de nível de obesidade")
    status: str = Field("success", description="Status da requisição")
