from ml.Fonctions import load_data,clean_data,split_data,Matrice_confusion,ROC_curve,Classification_Report
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score ,f1_score
import mlflow
import joblib
import os
from imblearn.over_sampling import SMOTE
from imblearn.pipeline import Pipeline as ImbPipeline

import os

ARTIFACTS_DIR = "artifacts"
os.makedirs(ARTIFACTS_DIR, exist_ok=True)

os.makedirs("saved_models", exist_ok=True)


mlflow.set_experiment("Retention_IA_Experiment")





data = load_data("Attrition-RH-Data.csv")
df = clean_data(data)
X,X_train, X_test, y_train, y_test = split_data(df)

#  Pipeline Scikit-learn
numeric_columns = X.select_dtypes(include='number').columns.tolist()
catg_columns = X.select_dtypes(include='object').columns.tolist()

preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numeric_columns),
        ('cat', OneHotEncoder(), catg_columns)
    ],
)

models = {
    "Logistic Regression": LogisticRegression(max_iter=1000),
    "Random Forest": RandomForestClassifier(
        n_estimators=200, random_state=42
    )
}

# --- Entraînement et évaluation pour chaque modèle ---
best_model = None
best_score = 0
name_model = ""


for name, model in models.items():
   
 
    pipe_clf = ImbPipeline(steps=[
    ('preprocessor', preprocessor),
    ('smote', SMOTE(random_state=42)),
    ('classifier', model)
      ])
     # Entrainnement 
    pipe_clf.fit(X_train, y_train)
    with mlflow.start_run(run_name=name):
        mlflow.set_tag("run_description", "Garder toutes les colonnes et entraîner avec paramètres par défaut+ SMOTE")
        # Prediction
        y_pred = pipe_clf.predict(X_test)
        y_prob = pipe_clf.predict_proba(X_test)[:,1]
    
    
        f1 = f1_score(y_test, y_pred, average='binary')
        # mlflow.log_metric("f1_score", f1)
    
    
    
        # Log modèle
        mlflow.sklearn.log_model(pipe_clf, f"model_{name}")
        
        # Log confusion matrix, ROC et classification report
        Matrice_confusion(y_test, y_pred, name, ARTIFACTS_DIR)
        ROC_curve(y_test, y_prob, name, ARTIFACTS_DIR)
        Classification_Report(y_test, y_pred, name, ARTIFACTS_DIR)

    
    print(f"Modèle {name} logué avec F1 = {f1:.2f}")

      #  Sauvegarde du modèle avec joblib
    file_model = f"saved_models/{name}.pkl"
    joblib.dump(pipe_clf, file_model)
    print(f"Modèle {name} sauvegardé dans {file_model}")
