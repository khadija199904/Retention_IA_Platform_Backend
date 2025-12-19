import requests
from google import genai
from fastapi import HTTPException
from ..core.config import GEMINI_API_KEY
from ..schemas.generate_plan_schema import RetentionPlan


client = genai.Client(api_key=GEMINI_API_KEY)


def generate_retention_plan(prompt):
      

 try :
    response = client.models.generate_content(model="gemini-2.5-flash-lite", contents=prompt,config={
        "response_mime_type": "application/json",
        "response_json_schema": RetentionPlan.model_json_schema(),
        "temperature": 0.2 
    },)
    # Getsion de reponse mal formée
    if not response.parsed:
        raise ValueError("Réponse Gemini mal formée")
    result = response.parsed
    return   result
     
 except requests.ConnectionError:
        raise HTTPException(status_code=503, detail="Impossible de se connecter à Gemini")
  
 
    

