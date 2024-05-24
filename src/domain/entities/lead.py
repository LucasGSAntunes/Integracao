from typing import Dict
from datetime import datetime

from src.domain.entities.base_entity import Entity

class Lead(Entity):
    def __init__(
            self,
            name: str,
            phone: str,
            perguntas: str = "",
            source: str = "",
            created_at: str = "",
            updated_at: str = "",
            id: str = None,
            **kwargs
    ):
        _id = id
        self.id = str(_id) if _id else None

        now = datetime.utcnow().isoformat()
        self.created_at = now if not created_at else created_at
        self.updated_at = now if not updated_at else updated_at

        self.name = name
        self.phone = phone
        self.perguntas = perguntas
        self.source = source

    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "name": self.name,
            "phone": self.phone,
            "perguntas": self.perguntas,
            "source": self.source,
        }