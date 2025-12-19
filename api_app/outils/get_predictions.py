import os
import pandas as pd
from api_app.outils.load_model import load_model
from fastapi import HTTPException


MODEL_PATH = os.path.join("ml", "saved_models", "Logistic Regression.pkl")

def get_prediction(features):

    # Charge le modèle 
    model = load_model(MODEL_PATH)
    if model is None:
        raise HTTPException(status_code=503, detail="Le service de prédiction est indisponible (Modèle non chargé).")

    try:
        # Convertit l'objet Pydantic en DataFrame
        employee_data = pd.DataFrame([features.model_dump()])
        proba = model.predict_proba(employee_data)[0][1]  # probabilité de la classe "1" (churn)
        probability = round(proba, 2)

        return probability
    except ValueError as e:
        raise HTTPException(status_code=422, detail=f"Données incompatibles avec le modèle: {e}")
