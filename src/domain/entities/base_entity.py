from abc import ABC, abstractmethod


class Entity(ABC):
    @abstractmethod
    def is_valid(self) -> bool:
        pass
