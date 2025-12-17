from fastapi import APIRouter, HTTPException
import joblib
import pandas as pd
import os
from api_app.schemas.predict_schema import PredictionRequest, PredictionResponse
from api_app.outils.load_model import load_model




router = APIRouter()

MODEL_PATH = os.path.join("ml", "saved_models", "Logistic Regression.pkl")

@router.post("/predict",response_model=PredictionResponse)
def predict_churn(features: PredictionRequest):
    
    model = load_model(MODEL_PATH)
     
    if model is None:
        raise HTTPException(status_code=503, detail="Le service de prédiction est indisponible (Modèle non chargé).")
    
    try:

        employee_data = pd.DataFrame([features.model_dump()])
        probability = model.predict_proba(employee_data)[0][1] # probabilité de la classe "1" (churn)
        probability = round(probability , 2)

    except ValueError as e:
        # Si les dimensions ou types sont incompatibles avec le modèle
        raise HTTPException(
            status_code=422,
            detail=f"Données incompatibles avec le modèle: {e}"
        )
    
    

    return {
          "churn_probability" : probability
          }
   

    # return PredictionResponse(churn_probability=probability)