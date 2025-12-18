import os
import requests
from ..core.config import HF_API_TOKEN
from ..outils.generate_rh_prompt import generate_hr_prompt


if not HF_API_TOKEN:
    raise ValueError("La clé d'API Hugging Face n'est pas définie. Veuillez la mettre dans le fichier .env")
headers = {"Authorization": f"Bearer {HF_API_TOKEN}"}


API_URL = "https://router.huggingface.co/v1/chat/completions"






def generate(features,churn_proba):

    prompt_RH = generate_hr_prompt(features,churn_proba)

    # payload= { 
    #     "ch" : 
    # }
    
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

response = generate({
    "messages": [
        {
            "role": "user",
            "content": "What is the capital of France?"
        }
    ],
    "model": "meta-llama/Llama-3.1-8B-Instruct:novita"
})

print(response["choices"][0]["message"])