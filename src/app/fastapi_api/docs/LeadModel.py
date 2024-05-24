from typing import Dict

from pydantic import BaseModel

class LeadModel(BaseModel):
    name: str
    phone: str
    area: str
    id: str
    source: str
    pergunta: str
