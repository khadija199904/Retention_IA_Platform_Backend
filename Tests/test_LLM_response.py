
import os
from unittest.mock import Mock,patch
os.environ["GEMINI_API_KEY"] = "fake_key"
from api_app.services.generative_IA import client, generate_retention_plan

def test_API_LLMG(mocker):
    
    fake_response = Mock()
    fake_response.parsed = {"retention_plan": ["Plan 1", "Plan 2", "Plan 3"]}

    # Mock l'API Gemini
    
    mock = mocker.patch("api_app.services.generative_IA.client.models.generate_content", return_value=fake_response)

       # Appel de la fonction
    result = generate_retention_plan("test prompt")

       
    assert "retention_plan" in result
    assert len(result["retention_plan"]) == 3
   