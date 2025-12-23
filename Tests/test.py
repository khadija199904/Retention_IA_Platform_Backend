import pytest 
import pandas as pd 



def test_df () :

    df = pd.read_csv("ml/Attrition-RH-Data.csv")

    Valeur_M = df.isnull().sum().sum()
    
    Valeur_D = df.duplicated().sum()


    assert Valeur_M == 0
    assert Valeur_D == 0
    




