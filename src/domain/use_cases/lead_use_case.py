from typing import Dict
from datetime import datetime
import json

from src.domain.interfaces.abstract_repositories import ABCLeadRepository
from src.domain.entities.lead import Lead

class LeadUseCase:
    repository: None

    def __init__(self):
        self.data_acess: ABCLeadRepository = self.repository
    
    def create_lead(
            self, 
            name: str, 
            phone: str, 
            perguntas: Dict[str, str],
            id: str = None
        ) -> Dict:
        source = "Respondi"

        lead = Lead(name, phone, perguntas, id, source)
        return self.data_acess.create(lead)
    
    def webhook(
            self, 
            name: str, 
            phone: str, 
            perguntas: Dict[str, str],
            id: str = None
        ) -> Dict:
        source = "Respondi"

        lead = Lead(name, phone, perguntas, id, source)

        return self.data_acess.create(lead)