from fastapi import APIRouter, HTTPException ,Depends
from ..schemas.employe_schema import EmployeeData
from ..schemas.generate_plan_schema import RetentionPlan
from ..outils.build_rh_prompt import build_rh_prompt
from ..services.generative_IA import generate_retention_plan
from api_app.outils.get_predictions import get_prediction
from api_app.core.security import verify_token



router = APIRouter( tags=["Generative IA"])


@router.post('/generate-retention-plan', response_model=RetentionPlan)
async def generate_rh_plan(request : EmployeeData,token = Depends(verify_token)):
    try:
          # Obtenir la probabilité de churn via endpoint /predict
            churn_proba = get_prediction(request)
            if churn_proba is None:
                raise HTTPException(status_code=500, detail="Churn probability introuvable")
        
            churn_proba = churn_proba *100 # convertir en %
    
            # la condition logique 
            if churn_proba > 50 :

              #  Construire prompt dynamique
               prompt = build_rh_prompt(request, churn_proba)

               # Générer plan RH via LLM
               plan = generate_retention_plan(prompt)
     
            



            return RetentionPlan(**plan)
    
    except HTTPException:
        raise
    except Exception as e:
        # Catch-all pour toute erreur inattendue
        raise HTTPException(status_code=500, detail=f"Erreur interne : {e}")