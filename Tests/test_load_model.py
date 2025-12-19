import pytest
import os
from fastapi import HTTPException
from api_app.outils.load_model import load_model  

# Définir le chemin du modèle
MODEL_PATH = os.path.join("ml", "saved_models", "Logistic Regression.pkl")

def test_load_model_success():
    
    model = load_model(MODEL_PATH)
    assert model is not None