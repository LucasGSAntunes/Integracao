from typing import Dict

from src.domain.entities.base_entity import Entity

class Lead(Entity):
    def __init__(
            self,
            name: str,
            phone: str,
            descricao: Dict,
            id: str = None,
            source: str = "",
    ):
        _id = id
        self.id = str(_id) if _id else None

        self.name = name
        self.phone = phone
        self.descricao = descricao
        self.source = source

    def is_valid(self) -> bool:
        return all([
            self.name,
            self.phone,
            self.descricao,
            self.source,
        ])

    def to_dict(self) -> Dict:
        return {
            "name": self.name,
            "phone": self.phone,
            "descricao": self.descricao,
            "source": self.source,
            "id": self.id,
        }