import joblib
import os
from fastapi import HTTPException,status

def load_model(model_path):
    if not os.path.exists(model_path):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Modèle du Prediction introuvable : {model_path}"
        )
    try:
        # 2. Charger le modèle
        model = joblib.load(model_path)
        
        return model
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Le fichier du modèle est invalide ou corrompu: {e}" 
        ) 

    except Exception as e:
        
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erreur interne lors du chargement du modèle: {e}"
        )




if __name__ == "__main__":

    MODEL_PATH = os.path.join("ml", "saved_models", "Logistic Regression.pkl")
    load_model(MODEL_PATH)
