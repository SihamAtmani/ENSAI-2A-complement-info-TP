from business_object.attaques.abstract_attack import AbstractAttack


class FixedDamageAttack(AbstractAttack):
    def __init__(self, power: int, name: str, description: str):
        super().__init__(power, name, description)

    def compute_damage(self, attacker, defender) -> int:
        return self._power
