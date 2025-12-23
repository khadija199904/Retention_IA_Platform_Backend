from ml.Fonctions import load_data,clean_data,split_data,Matrice_confusion,ROC_curve,Classification_Report
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import recall_score
import mlflow
import joblib
import os
from imblearn.over_sampling import SMOTE
from imblearn.pipeline import Pipeline as ImbPipeline
from sklearn.model_selection import GridSearchCV

import os

ARTIFACTS_DIR = "artifacts"
os.makedirs(ARTIFACTS_DIR, exist_ok=True)

os.makedirs("saved_models", exist_ok=True)


mlflow.set_experiment("Retention_IA_Experiment")





data = load_data("ml/Attrition-RH-Data.csv")
df = clean_data(data)
X,X_train, X_test, y_train, y_test = split_data(df)


#  Pipeline Scikit-learn

ordinal_cols = ['EnvironmentSatisfaction','JobInvolvement','JobSatisfaction']
X_new = X.drop(columns=ordinal_cols)
catg_cols = X.select_dtypes(include='object').columns.tolist()
numeric_cols = X_new.select_dtypes(include='number').columns.tolist()


preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numeric_cols),
        ('ordinal', 'passthrough', ordinal_cols),
        ('cat', OneHotEncoder(), catg_cols)
        
    ],
    remainder="passthrough"
)


models_params = {
    "Logistic Regression": {
        "model": LogisticRegression(max_iter=1000),
        "params": {
            "classifier__C":  [0.01, 0.1, 1, 10,20],
        }
    },
    "Random Forest": {
        "model": RandomForestClassifier(random_state=42),
        "params": {
            "classifier__n_estimators": [50, 100],
            "classifier__max_depth": [5, 10, 20],
            "classifier__min_samples_leaf": [5, 8, 14],
        }
    }
}


#  Entraînement et évaluation pour chaque modèle 

for name, config in models_params.items():
    
    
    model = config["model"]
    params = config["params"]
 
    pipe_clf = ImbPipeline(steps=[
    ('preprocessor', preprocessor),
    ('smote', SMOTE(random_state=42)),
    ('classifier', model)
      ])
     # Entrainnement 
    
    with mlflow.start_run(run_name=name):
        mlflow.set_tag("run_description", "Optimisation par GridSearchCV et SMOTE avec sélection de variables (suppression des colonnes non-pertinentes et faiblement corrélées")
        # Prediction
        grid = GridSearchCV(pipe_clf, param_grid=params, cv=3 , scoring='recall', n_jobs=-1)
        grid.fit(X_train, y_train)
        
        best_pipe = grid.best_estimator_
       
        # Évaluation
        y_pred = best_pipe.predict(X_test)
        y_prob = best_pipe.predict_proba(X_test)[:, 1]
    
        mlflow.log_params(grid.best_params_)
        # Log modèle
        mlflow.sklearn.log_model(best_pipe, f"model_{name}")

        # Log confusion matrix, ROC et classification report
        Matrice_confusion(y_test, y_pred, name, ARTIFACTS_DIR)
        ROC_curve(y_test, y_prob, name, ARTIFACTS_DIR)
        Classification_Report(y_test, y_pred, name, ARTIFACTS_DIR)

         # 5. Calcul et affichage du F1 final
        recall = recall_score(y_test, y_pred)
        print(f"Modèle {name} optimisé - recall: {recall:.2f}")

        # 6. Sauvegarde  modèle optimisé avec joblib
        file_model = f"saved_models/{name}_optimized.pkl"
        joblib.dump(best_pipe, file_model)
        print(f"Sauvegardé : {file_model}")
      
   
