from typing import Dict
from datetime import datetime
import json

from src.domain.interfaces.abstract_repositories import ABCLeadRepository
from src.domain.entities.lead import Lead
from src.infra.lead_repository import LeadRepository

class LeadUseCase:
    def __init__(self, repository: ABCLeadRepository):
        self.repository = repository
        self.data_acess = repository
    
    def create_lead(
            self, 
            name: str, 
            phone: str, 
            area: str,
            id: str = None,
            pergunta: str = None,
        ) -> Dict:
        source = "Respondi"
        descricao = {
            "area": area,
            "pergunta": pergunta,
        }

        lead = Lead(name, phone, descricao, id, source)
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