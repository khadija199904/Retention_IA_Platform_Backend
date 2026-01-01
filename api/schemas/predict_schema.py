from pydantic import BaseModel,Field

    
class PredictionResponse(BaseModel):
    churn_probability: float


