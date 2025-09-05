from abc import ABC, abstractmethod

class AbstractAttack(ABC):
    def __init__(self, power: int, name: str, description: str):
        self._power = power
        self._name = name
        self._description = description

    @abstractmethod
    def compute_damage(self, attack, defense) -> int:
        pass


