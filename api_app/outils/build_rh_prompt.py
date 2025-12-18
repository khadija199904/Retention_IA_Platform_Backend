from ..schemas.predict_schema import PredictionRequest

def build_rh_prompt(data: PredictionRequest, churn_probability: float) :
    # On construit le prompt avec une f-string
    satisfaction_ref = {1: "Faible (Low)", 2: "Moyen (Medium)", 3: "Élevé (High)", 4: "Très Élevé (Very High)"}
    wlb_map = {1: "Mauvais (Bad)", 2: "Bon (Good)", 3: "Meilleur (Better)", 4: "Excellent (Best)"}
    
    prompt = f"""
Agis comme un expert RH.

Voici les informations sur l employé :
- Age : {data.Age} ans
- Genre : {data.Gender}
- Situation : {data.MaritalStatus}, habite à {data.DistanceFromHome} km
- Département : {data.Department}
- Role : {data.JobRole} (Niveau {data.JobLevel})
- Déplacements : {data.BusinessTravel}
- Heures Supplémentaires : {data.OverTime}

SATISFACTION & PERFORMANCE :
- Satisfaction Job : {data.JobSatisfaction}/4 ({satisfaction_ref.get(data.JobSatisfaction)})
- Environnement : {data.EnvironmentSatisfaction}/4 ({satisfaction_ref.get(data.EnvironmentSatisfaction)})
- Relations : {data.RelationshipSatisfaction}/4 ({satisfaction_ref.get(data.RelationshipSatisfaction)})
- Performance : {data.PerformanceRating}/4
- Équilibre Vie Pro/Perso : {data.WorkLifeBalance}/4 ({wlb_map.get(data.WorkLifeBalance)})

CONTEXTE FINANCIER & CARRIÈRE :
- Salaire Mensuel : {data.MonthlyIncome}
- Dernière augmentation : {data.PercentSalaryHike}%
- Stock Options : Niveau {data.StockOptionLevel}
- Ancienneté : {data.YearsAtCompany} ans ({data.YearsInCurrentRole} ans au poste actuel)
- Dernière promotion : il y a {data.YearsSinceLastPromotion} ans
- Formations l'an dernier : {data.TrainingTimesLastYear}

Contexte : ce salarié a un risque élevé de (Churn Probability : {churn_probability}%) de départ selon le modèle ML.

Tache : propose 3 actions concrètes et personnalisées pour le retenir dans l entreprise, en tenant compte de son role, sa satisfaction, sa performance et son équilibre vie professionnelle/personnelle.
Rédige les actions de façon claire et opérationnelle pour un manager RH. Réponds uniquement avec le plan d'action au format JSON (liste de chaines de caractères).
"""
    return prompt
