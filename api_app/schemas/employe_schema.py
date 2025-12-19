from pydantic import BaseModel,Field

class EmployeeData(BaseModel):
    #   Informations 
    Age: int = Field(...)
    DailyRate: int = Field(...)
    DistanceFromHome: int = Field(...)

    # --- Satisfaction & Rôle (avec descriptions fournies) ---
    EnvironmentSatisfaction: int = Field(
        ..., ge=1, le=4, 
        description="1 'Low' 2 'Medium' 3 'High' 4 'Very High'"
    )
    JobInvolvement: int = Field(
        ..., ge=1, le=4, 
        description="1 'Low' 2 'Medium' 3 'High' 4 'Very High'"
    )
    JobLevel: int = Field(...)
    JobRole: str = Field(..., example="Sales Executive")
    JobSatisfaction: int = Field(
        ..., ge=1, le=4, 
        description="1 'Low' 2 'Medium' 3 'High' 4 'Very High'"
    )
    
    # --- Statut et Salaire ---
    MaritalStatus: str = Field(..., example="Single")
    MonthlyIncome: int = Field(..., example=5993)
    OverTime: str = Field(..., example="Yes")
    StockOptionLevel: int = Field(..., example=0)
    
    # --- Historique et Ancienneté ---
    TotalWorkingYears: int = Field(..., example=8)
    YearsAtCompany: int = Field(..., example=6)
    YearsInCurrentRole: int = Field(..., example=4)
    YearsWithCurrManager: int = Field(..., example=5)