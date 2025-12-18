from fastapi import APIRouter, HTTPException ,Depends
from ..schemas.predict_schema import PredictionRequest
import requests
from ..outils.build_rh_prompt import build_rh_prompt
from ..services.generative_IA import generate_retention_plan



router = APIRouter()


@router.post('/generate-retention-plan')
async def generate_rh_plan(request : PredictionRequest):

    # Obtenir la probabilité de churn via endpoint /predict

    PREDICT_URL = "http://localhost:8000/predict"
    predict_response = requests.post(PREDICT_URL, json=request.dict())
    if predict_response.status_code != 200:
        raise HTTPException(status_code=500, detail="Erreur lors de la prédiction")
    churn_prob = predict_response.json()["churn_probability"]
    churn_prob = churn_prob *100 # convertir en %
    
    # la condition logique 
    if churn_prob > 50 :

       #  Construire prompt dynamique
        prompt = build_rh_prompt(request.dict(), churn_prob)

       # Générer plan RH via LLM
        plan = generate_retention_plan(prompt)
     
        print(plan)



        return True