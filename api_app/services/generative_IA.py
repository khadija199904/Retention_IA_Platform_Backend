import os

from openai import OpenAI
from ..core.config import HF_API_TOKEN

import os
from openai import OpenAI
from ..schemas.generate_plan_schema import RetentionPlan



if not HF_API_TOKEN:
    raise ValueError("La clé d'API Hugging Face n'est pas définie. Veuillez la mettre dans le fichier .env")

client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key= HF_API_TOKEN,
)



def generate_retention_plan(prompt):

        
   
        completion = client.chat.completions.parse(
            model="meta-llama/Llama-3.1-8B-Instruct:novita",
            messages=[
                {"role": "system", 
                 "content": "TRéponds UNIQUEMENT en JSON avec la clé 'retention_plan' (liste de chaînes)."
                 },
                {"role": "user","content": prompt}
             ],
            response_format=RetentionPlan,
            temperature=0.2
       )
    
        result = completion.choices[0].message.parsed
        
        return result

    
    

