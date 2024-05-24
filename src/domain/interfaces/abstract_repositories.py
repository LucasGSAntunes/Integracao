from abc import ABC, abstractmethod
from typing import Dict

from src.domain.entities.lead import Lead

class ABCLeadRepository(ABC):
    @abstractmethod
    def create(self, lead: Lead) -> Dict:
        pass

    