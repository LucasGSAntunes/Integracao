from pydantic import BaseModel
from typing import Dict

class Lead(BaseModel):
    name: str
    phone: str
    perguntas: Dict[str, str]