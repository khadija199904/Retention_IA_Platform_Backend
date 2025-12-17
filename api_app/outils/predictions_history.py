from sqlalchemy.orm import Session
from api_app.models.users import PredictionHistory

def save_prediction_history(db: Session, userid: int, employeeid: int, probability: float) :
    
    pred_history = PredictionHistory(
        userid=userid,
        employeeid=employeeid,
        probability=probability
    )
    db.add(pred_history)
    db.commit()
    db.refresh(pred_history)  
    return pred_history
