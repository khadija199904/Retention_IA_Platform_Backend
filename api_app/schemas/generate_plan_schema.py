from pydantic import BaseModel 
from typing import List




class RetentionPlan(BaseModel):
    retention_plan: List[str]



 