import pandas as pd 
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, roc_curve, roc_auc_score, classification_report
import mlflow

def load_data(filepath):
    df = pd.read_csv(filepath)
    return df 

def clean_data (df) :
    df_cleaned = df.copy()
    # Supprimer les collones unitile
    cols_to_drop = ['EmployeeCount','EmployeeNumber','Over18','StandardHours']
    df_cleaned = df_cleaned.drop(columns=cols_to_drop)

    return df_cleaned

def split_data(df):

    X = df.drop(columns=['Attrition'])
    y = df['Attrition']

    # Transformation de la cible
    y = y.map({'No':0, 'Yes':1})

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    return X,X_train, X_test, y_train, y_test


def Matrice_confusion(y_true, y_pred,model_name,artifacts_dir ):
    cm = confusion_matrix(y_true, y_pred)
    plt.figure(figsize=(5,4))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.title("Confusion Matrix")
    file_cm = f"{artifacts_dir}/confusion_matrix_{model_name}.png"
    plt.savefig(file_cm)
    mlflow.log_artifact(file_cm)
    plt.close()

    return

def ROC_curve(y_true, y_prob,model_name,artifacts_dir):
    fpr, tpr, thresholds = roc_curve(y_true, y_prob)
    roc_score = roc_auc_score(y_true, y_prob)
    plt.figure(figsize=(6,4))
    plt.plot(fpr, tpr, label=f'AUC = {roc_score:.2f}')
    plt.plot([0,1], [0,1], '--', color='gray')
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.title("ROC Curve")
    plt.legend()
    file_ROC = f"{artifacts_dir}/roc_curve_{model_name}.png"
    plt.savefig(file_ROC)
    mlflow.log_artifact(file_ROC)
    # mlflow.log_metric("roc_auc", roc_score)
    plt.close()


# Fonction pour le rapport de classification
def Classification_Report(y_true, y_pred,model_name,artifacts_dir):
    report = classification_report(y_true, y_pred, output_dict=True)
    
    metrics = ({
        "accuracy": report["accuracy"],                   # score global
        "precision": report["1"]["precision"], # précision 
        "recall": report["1"]["recall"],       # rappel 
        "f1_score": report["1"]["f1-score"]    # F1 
    })
    mlflow.log_metrics(metrics)
     # Sauvegarde le report texte
    file_report = f"{artifacts_dir}/classification_report_{model_name}.txt"
    with open(file_report, "w") as f:
        f.write(classification_report(y_true, y_pred))

    # Log dans MLflow
    mlflow.log_artifact(file_report)
    return report
