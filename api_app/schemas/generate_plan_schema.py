from pydantic import BaseModel ,List


class generateRequest(BaseModel):
    churn_probability : float
    prompt : str 

class generateResponse(BaseModel):
    retention_plan: List[str]



 