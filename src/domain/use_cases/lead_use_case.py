from typing import Dict
from datetime import datetime
import json

from src.domain.interfaces.abstract_repositories import ABCLeadRepository
from src.domain.entities.lead import Lead
from src.infra.lead_repository import LeadRepository

class LeadUseCase:
    repository: ABCLeadRepository = LeadRepository()

    def __init__(self):
        self.data_acess: ABCLeadRepository = LeadRepository()
    
    def create_lead(
            self, 
            name: str, 
            phone: str, 
            area: str,
            id: str = None,
            pergunta: str = None,
        ) -> Dict:
        source = "Respondi"
        descricao = f'{id}: {area}, {pergunta}'


        lead = Lead(name, phone, descricao, id, source)
        
        if not lead.is_valid():
            return {"message": "lead isn't valid"}
        
        return self.data_acess.create(lead)
    