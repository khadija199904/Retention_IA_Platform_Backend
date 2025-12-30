from pydantic import BaseModel, Field, ConfigDict

class EmployeeData(BaseModel):
    # --- Informations de base & Démographie ---
    employeeid: int = Field(...)
    Age: int = Field(..., ge=18, le=70)
    MaritalStatus: str = Field(..., example="Single", description="Single, Married, or Divorced")
    DistanceFromHome: int = Field(..., ge=1, description="Distance du domicile en km")

    # --- Parcours Professionnel & Éducation ---
    Department: str = Field(..., example="Research & Development")
    EducationField: str = Field(..., example="Life Sciences")
    BusinessTravel: str = Field(..., example="Travel_Rarely", description="Non-Travel, Travel_Rarely, Travel_Frequently")
    
    # --- Rôle & Satisfaction (Échelles de 1 à 4) ---
    JobRole: str = Field(..., example="Sales Executive")
    JobLevel: int = Field(..., ge=1, le=5)
    
    EnvironmentSatisfaction: int = Field(
        ..., ge=1, le=4, 
        description="1 'Low' 2 'Medium' 3 'High' 4 'Very High'"
    )
    JobInvolvement: int = Field(
        ..., ge=1, le=4, 
        description="1 'Low' 2 'Medium' 3 'High' 4 'Very High'"
    )
    JobSatisfaction: int = Field(
        ..., ge=1, le=4, 
        description="1 'Low' 2 'Medium' 3 'High' 4 'Very High'"
    )
    WorkLifeBalance: int = Field(
        ..., ge=1, le=4, 
        description="1 'Bad' 2 'Good' 3 'Better' 4 'Best'"
    )

    # --- Rémunération & Temps de Travail ---
    DailyRate: int = Field(..., example=1102)
    MonthlyIncome: int = Field(..., example=5993)
    OverTime: str = Field(..., example="Yes", description="Yes or No")
    StockOptionLevel: int = Field(..., ge=0, le=3)

    # --- Historique & Performance ---
    TotalWorkingYears: int = Field(..., ge=0)
    TrainingTimesLastYear: int = Field(..., ge=0, description="Nombre de formations l'année dernière")
    YearsAtCompany: int = Field(..., ge=0)
    YearsInCurrentRole: int = Field(..., ge=0)
    YearsWithCurrManager: int = Field(..., ge=0)

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "employeeid": 1,
                "Age": 41,
                "BusinessTravel": "Travel_Rarely",
                "DailyRate": 1102,
                "Department": "Sales",
                "DistanceFromHome": 1,
                "EducationField": "Life Sciences",
                "EnvironmentSatisfaction": 2,
                "JobInvolvement": 3,
                "JobLevel": 2,
                "JobRole": "Sales Executive",
                "JobSatisfaction": 4,
                "MaritalStatus": "Single",
                "MonthlyIncome": 5993,
                "OverTime": "Yes",
                "StockOptionLevel": 0,
                "TotalWorkingYears": 8,
                "TrainingTimesLastYear": 0,
                "WorkLifeBalance": 1,
                "YearsAtCompany": 6,
                "YearsInCurrentRole": 4,
                "YearsWithCurrManager": 5
            }
        }
    )