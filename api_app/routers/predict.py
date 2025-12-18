from fastapi import APIRouter, HTTPException ,Depends
from sqlalchemy.orm import Session
from api_app.schemas.predict_schema import PredictionRequest, PredictionResponse
from api_app.dependencies import get_db
from api_app.core.security import verify_token
from api_app.outils.get_predictions import get_prediction
from api_app.outils.predictions_history import save_prediction_history
from api_app.models.users import USERS





router = APIRouter()



@router.post("/predict",response_model=PredictionResponse)
async def predict_churn(features: PredictionRequest,token = Depends(verify_token),db: Session = Depends(get_db)):
    username = token["Username"]
    
    try:
        # Chercher l'utilisateur en base
        user = db.query(USERS).filter(USERS.username == username).first()
        if not user:
            raise HTTPException(status_code=404, detail="Utilisateur introuvable")

        # Récupérer l'id réel
        userid = user.id
        employeeid = features.employeeid
        probability = get_prediction(features)
        save_prediction_history(db=db, userid=userid, employeeid=employeeid, probability=probability)
        # save_prediction_history(db=db, user_id=userid, probability=probability)

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