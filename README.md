# Retention_IA_Platform_Backend
Application Fullstack (Cote Backend) d'aide à la décision RH combinant ML supervisé pour la prédiction des départs et GenAI pour l'assistance stratégique
#  RetentionAI - Backend API

##  Présentation
RetentionAI est le moteur d'intelligence décisionnelle pour les RH. Ce backend expose une API REST sécurisée permettant de prédire le risque de départ des employés et de générer des stratégies de rétention via l'IA Générative.

##  Stack Technique
- **Framework :** FastAPI (Python 3.10+)
- **Machine Learning :** Scikit-Learn, Pandas, MLflow
- **IA Générative :** Google Gemini API / Hugging Face Inference API
- **Base de données :** PostgreSQL (SQLAlchemy)
- **Sécurité :** JWT (JSON Web Tokens) & Bcrypt
- **Conteneurisation :** Docker / Docker-compose

##  Fonctionnalités
- **Authentification :** Système complet d'inscription et de connexion pour les managers RH.
- **Prediction Engine :** Modèle Random Forest optimisé pour calculer la probabilité de "churn".
- **GenAI Advisor :** Génération de plans d'actions personnalisés si le risque dépasse 50%.
- **Historisation :** Sauvegarde de chaque prédiction dans PostgreSQL pour un suivi temporel.

## Installation & Lancement

### 1. Cloner le projet
```bash
git clone https://github.com/khadija199904/Retention_IA_Platform_Backend.git
cd Retention_IA_Platform_Backend
```
### 2. Variables d'environnement
```bash
POSTGRES_USER=USE
POSTGRES_PASSWORD=PASSWORD
POSTGRES_HOST=localhost
POSTGRES_DB=DN_NAME
POSTGRES_PORT=PORT

HUGGINGFACE_API_TOKEN="hf_**************************************"
SECRET_KEY = "************************"
```

### 3. Lancement avec Docker (Recommandé)
```bash
 docker-compose up --build
```
L'API sera accessible sur http://localhost:8000. La documentation Swagger est disponible sur /docs.

## Tests
```bash
pytest -v
```


