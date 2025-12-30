from ..schemas.employe_schema import EmployeeData


def build_rh_prompt(data: EmployeeData, churn_probability: float):
    
    satisfaction_map = {1: "Low", 2: "Medium", 3: "High", 4: "Very High"}
    #  JobInvolvement utilise la même échelle que satisfaction 
    wlb_map = {1: "Bad",2: "Good", 3: "Better", 4: "Best"}
    prompt = f"""
   Agis comme un expert RH.

   Voici les informations sur l'employé  :

INFORMATIONS PERSONNELLES :
- Âge : {data.Age} ans
- Situation familiale : {data.MaritalStatus}
- Distance domicile-travail : {data.DistanceFromHome} km

CONTEXTE PROFESSIONNEL :
- Département : {data.Department}
- Domaine d'éducation : {data.EducationField}
- Déplacements : {data.BusinessTravel}
- Rôle : {data.JobRole} (Niveau {data.JobLevel})

SATISFACTION & ENGAGEMENT :
- Satisfaction Job : {data.JobSatisfaction}/4 ({satisfaction_map.get(data.JobSatisfaction)})
- Satisfaction Environnement : {data.EnvironmentSatisfaction}/4 ({satisfaction_map.get(data.EnvironmentSatisfaction)})
- Implication (Job Involvement) : {data.JobInvolvement}/4 ({satisfaction_map.get(data.JobInvolvement)})
- Work Life Balance : {data.WorkLifeBalance}/4 ({wlb_map.get(data.WorkLifeBalance)})

RÉMUNÉRATION & TEMPS DE TRAVAIL :
- Salaire Mensuel : {data.MonthlyIncome}
- Taux Journalier : {data.DailyRate}
- Heures Supplémentaires : {data.OverTime}
- Stock Options : Niveau {data.StockOptionLevel}

EXPÉRIENCE & HISTORIQUE :
- Expérience Totale : {data.TotalWorkingYears} ans
- Ancienneté Entreprise : {data.YearsAtCompany} ans
- Années au poste actuel : {data.YearsInCurrentRole} ans
- Années avec le manager actuel : {data.YearsWithCurrManager} ans
- Formations suivies l'année dernière : {data.TrainingTimesLastYear}

Contexte : Ce salarié a un risque de départ de {churn_probability}% selon le modèle ML.

Tâche : Propose exactement 3 actions RH très courtes, 1 phrase maximum chacune, directes et opérationnelles pour le retenir.
Prends en compte son engagement, sa relation avec son manager ({data.YearsWithCurrManager} ans), son équilibre vie pro/perso et son ancienneté.

Contraintes :
- Aucune explication ou justification.
- Réponds uniquement avec le plan d'action au format JSON : une liste contenant exactement 3 chaînes de caractères.
"""
    return prompt
