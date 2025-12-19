import pytest
from unittest.mock import Mock,patch
from api_app.services.generative_IA import client, generate_retention_plan

def test_API_LLMG():
    
    fake_response = Mock()
    fake_response.parsed = {
        "retention_plan": [
            "Proposer 2 jours de télétravail",
            "Réévaluer la charge de déplacement",
            "Plan de formation personnalisé"
        ]
    }

    # Mock l'API Gemini
    client.models.generate_content = Mock(return_value=fake_response)

    # Appel de la fonction
    result = generate_retention_plan("test prompt")

    # Assertions
    assert "retention_plan" in result
    assert len(result["retention_plan"]) == 3
    assert result["retention_plan"][0] == "Proposer 2 jours de télétravail"