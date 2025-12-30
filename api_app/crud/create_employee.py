from sqlalchemy.orm import Session
from api_app.models.employee import EmployeeTable
from api_app.schemas.employe_schema import EmployeeData 

def create_new_employee(db: Session, employee: EmployeeData):
    """
    Crée un employé en base de données et retourne l'objet créé avec son ID.
    """
    try:
        
        new_emp = EmployeeTable(**employee.model_dump())
        db.add(new_emp)
        db.commit()
        db.refresh(new_emp)
        
        return new_emp
    except Exception as e:
        
        db.rollback()
        raise e