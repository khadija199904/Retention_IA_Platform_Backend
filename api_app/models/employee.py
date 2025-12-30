from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import relationship
from api_app.database import Base



class EmployeeTable(Base):
    __tablename__ = "employees"

    # employeeid est la clé primaire
    employeeid = Column(Integer, primary_key=True, index=True)
    
    
    Age = Column(Integer)
    BusinessTravel = Column(String)
    DailyRate = Column(Integer)
    Department = Column(String)
    DistanceFromHome = Column(Integer)
    EducationField = Column(String)
    EnvironmentSatisfaction = Column(Integer)
    JobInvolvement = Column(Integer)
    JobLevel = Column(Integer)
    JobRole = Column(String)
    JobSatisfaction = Column(Integer)
    MaritalStatus = Column(String)
    MonthlyIncome = Column(Integer)
    OverTime = Column(String)
    StockOptionLevel = Column(Integer)
    TotalWorkingYears = Column(Integer)
    TrainingTimesLastYear = Column(Integer)
    WorkLifeBalance = Column(Integer)
    YearsAtCompany = Column(Integer)
    YearsInCurrentRole = Column(Integer)
    YearsWithCurrManager = Column(Integer)
    
    # Relation vers l'historique : permet de faire employee.predictions
    
    predictions = relationship("PredictionHistory", back_populates="employee")