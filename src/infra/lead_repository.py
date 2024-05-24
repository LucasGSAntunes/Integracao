from typing import Dict
import requests

from src.domain.entities.lead import Lead
from src.domain.interfaces.abstract_repositories import ABCLeadRepository

class LeadRepository(ABCLeadRepository):
    def create(self, lead: Lead) -> Dict:
        url = "https://api.exactspotter.com/v3/LeadsAdd"
        token = "d53a044d-913a-4e82-bf85-9bb30be1d74f"

        headers = {
            "Content-Type": "application/json",
            "token_exact": token,
        }
        
        print(lead.to_dict())

        request = {
            "duplicityValidation": "true",
            "lead": {
                "name": lead.name,
                "ddiPhone": "55",
                "phone": lead.phone,
                "description": lead.descricao,
                "source": lead.source,
            }
        }

        response = requests.post(url, headers=headers, json=request)
        
        print(response.json())

        if response.status_code == 200:
            return response.json()
        else:
            return {"message": "error", "response": response.text}
