from pydantic import BaseModel 
from typing import List


class RetentionPlanRequest(BaseModel):
    churn_probability : float
    prompt : str 

class RetentionPlan(BaseModel):
    retention_plan: List[str]



 