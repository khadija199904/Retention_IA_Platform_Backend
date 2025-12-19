from ..schemas.employe_schema import EmployeeData


def build_rh_prompt(data: EmployeeData, churn_probability: float):
    
    satisfaction_map = {1: "Low", 2: "Medium", 3: "High", 4: "Very High"}
    #  JobInvolvement utilise la même échelle que satisfaction 
    
    prompt = f"""
Agis comme un expert RH. 

Voici les informations sur l'employé (ID: {data.employeeid}) :
- Age : {data.Age} ans
- Situation : {data.MaritalStatus}, habite à {data.DistanceFromHome} km
- Role : {data.JobRole} (Niveau {data.JobLevel})
- Heures Supplémentaires : {data.OverTime}

SATISFACTION & ENGAGEMENT :
- Satisfaction Job : {data.JobSatisfaction}/4 ({satisfaction_map.get(data.JobSatisfaction)})
- Environnement : {data.EnvironmentSatisfaction}/4 ({satisfaction_map.get(data.EnvironmentSatisfaction)})
- Implication (Job Involvement) : {data.JobInvolvement}/4 ({satisfaction_map.get(data.JobInvolvement)})

CONTEXTE CARRIÈRE & FINANCIER :
- Salaire Mensuel : {data.MonthlyIncome} (Taux journalier : {data.DailyRate})
- Stock Options : Niveau {data.StockOptionLevel}
- Expérience Totale : {data.TotalWorkingYears} ans
- Ancienneté Entreprise : {data.YearsAtCompany} ans
- Années au poste actuel : {data.YearsInCurrentRole} ans
- Années avec le manager actuel : {data.YearsWithCurrManager} ans

Contexte : Ce salarié a un risque de départ de {churn_probability}% selon le modèle ML.

Tâche : Propose **exactement 3 actions RH très courtes**, **1 phrase maximum chacune**, **directes et opérationnelles** pour le retenir. 
Prends en compte son implication, sa relation avec son manager ({data.YearsWithCurrManager} ans) et son ancienneté.

Contraintes : 
- Ne fais **aucune explication ou justification**.
- Réponds uniquement avec le plan d'action au format JSON (liste de 3 chaînes de caractères).
"""
    return prompt
