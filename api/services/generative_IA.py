import time
import requests
from google import genai
from fastapi import HTTPException
from google.genai import errors
from ..core.config import GEMINI_API_KEY
from ..schemas.generate_plan_schema import RetentionPlan


client = genai.Client(api_key=GEMINI_API_KEY)


def generate_retention_plan(prompt):
      
  for attempt in range(2):
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
        except Exception as e:
            #  erreur de Quota (429)
            if "429" in str(e) or "RESOURCE_EXHAUSTED" in str(e):
                if attempt == 0: 
                    print("Quota atteint, attente de 15 secondes...")
                    time.sleep(15) 
                    continue
                else:
                    raise HTTPException(status_code=429, detail="Quota Gemini épuisé. Réessayez dans une minute.")
        except requests.ConnectionError:
          raise HTTPException(status_code=503, detail="Impossible de se connecter à Gemini")
  
 
    

