from fastapi import APIRouter, HTTPException ,Depends
from sqlalchemy.orm import Session
from api.schemas.predict_schema import  PredictionResponse
from api.schemas.employe_schema import EmployeeData 
from api.dependencies import get_db
from api.core.security import verify_token
from api.outils.get_predictions import get_prediction
from api.outils.predictions_history import save_prediction_history
from api.models.users import USERS 
from api.models.employee import EmployeeTable
from api.crud.create_employee import create_new_employee





router = APIRouter( tags=["Predictions"])



@router.post("/predict",response_model=PredictionResponse)
async def predict_churn(features: EmployeeData,token = Depends(verify_token),db: Session = Depends(get_db)):
    
    username = token["Username"]
    
    try:
        # Chercher l'utilisateur en base
        user = db.query(USERS).filter(USERS.username == username).first()
        if not user:
            raise HTTPException(status_code=404, detail="Utilisateur introuvable")
        
        new_employee = create_new_employee(db, features)
        emp_id = new_employee.employeeid
        

        probability = get_prediction(features)
        save_prediction_history(db=db, userid=user.id, employeeid=emp_id, probability=probability)
        

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