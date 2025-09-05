from business_object.attaques.abstract_attack import AbstractAttack
from business_object.statistic import Statistic

class TestFixedDamageAttack:
    def test_compute_damage(self):
        # GIVEN
        attack = AbstractAttack(50, "Tackle", "A simple attack")

        # WHEN
        damage = attack.compute_damage(None, None)
        
        # THEN
        assert damage == 50


if __name__ == "__main__":
    import pytest

    pytest.main([__file__])