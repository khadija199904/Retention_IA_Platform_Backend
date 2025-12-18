from pydantic import BaseModel,Field

class PredictionRequest(BaseModel):
    # --- Infos Personnelles ---
    employeeid: int = Field(..., example=22)
    Age: int = Field(..., example=41)
    Gender: str = Field(..., example="Female")
    MaritalStatus: str = Field(..., example="Single")
    DistanceFromHome: int = Field(..., example=1)

    # --- Éducation ---
    Education: int = Field(..., description="1 'Below College' 2 'College' 3 'Bachelor' 4 'Master' 5 'Doctor'", example=2)
    EducationField: str = Field(..., example="Life Sciences")

    # --- Poste ---
    Department: str = Field(..., example="Sales")
    JobRole: str = Field(..., example="Sales Executive")
    JobLevel: int = Field(..., example=2)
    BusinessTravel: str = Field(..., example="Travel_Rarely")

    # --- Satisfaction & Performance (avec descriptions) ---
    EnvironmentSatisfaction: int = Field(..., ge=1, le=4, description="1 'Low' 2 'Medium' 3 'High' 4 'Very High'", example=2)
    JobSatisfaction: int = Field(..., ge=1, le=4, description="1 'Low' 2 'Medium' 3 'High' 4 'Very High'", example=4)
    RelationshipSatisfaction: int = Field(..., ge=1, le=4, description="1 'Low' 2 'Medium' 3 'High' 4 'Very High'", example=1)
    JobInvolvement: int = Field(..., ge=1, le=4, description="1 'Low' 2 'Medium' 3 'High' 4 'Very High'", example=3)
    PerformanceRating: int = Field(..., ge=1, le=4, description="1 'Low' 2 'Good' 3 'Excellent' 4 'Outstanding'", example=3)
    WorkLifeBalance: int = Field(..., ge=1, le=4, description="1 'Bad' 2 'Good' 3 'Better' 4 'Best'", example=1)

    # --- Rémunération ---
    MonthlyIncome: int = Field(..., example=5993)
    DailyRate: int = Field(..., example=1102)
    HourlyRate: int = Field(..., example=94)
    MonthlyRate: int = Field(..., example=19479)
    PercentSalaryHike: int = Field(..., example=11)
    StockOptionLevel: int = Field(..., example=0)
    OverTime: str = Field(..., example="Yes")

    # --- Historique ---
    TotalWorkingYears: int = Field(..., example=8)
    TrainingTimesLastYear: int = Field(..., example=0)
    NumCompaniesWorked: int = Field(..., example=8)
    YearsAtCompany: int = Field(..., example=6)
    YearsInCurrentRole: int = Field(..., example=4)
    YearsSinceLastPromotion: int = Field(..., example=0)
    YearsWithCurrManager: int = Field(..., example=5)
    
class PredictionResponse(BaseModel):
    churn_probability: float


