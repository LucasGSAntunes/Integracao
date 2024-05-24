from src.domain.use_cases.lead_use_case import LeadUseCase

from src.infra.lead_repository import LeadRepository

def dependency_injection():
    LeadUseCase.repository = LeadRepository()