from typing import Dict

from pydantic import BaseModel

class LeadModel(BaseModel):
    name: str
    phone: str
    perguntas: Dict
    id: int
    source: str
    created_at: str
    updated_at: str
