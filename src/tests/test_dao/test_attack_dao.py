from dao.attack_dao import AttackDao
from business_object.attack.physical_attack import PhysicalFormulaAttack
class TestAttackDao:
    def test_find_attack_by_id_ok(self):
        # GIVEN
        existing_id_attack = 1

        # WHEN
        attack = AttackDao().find_attack_by_id(existing_id_attack)

        # THEN
        assert attack is not None
        assert attack.id == existing_id_attack

    # Create a test for method add_attack()

    def test_add_attack(self):
    # GIVEN 
        dao = AttackDao()
        fake_attack = PhysicalFormulaAttack(   
            power=50,
            name = "test2",
            description = "testtt2" , 
            accuracy=10,
            element="foudre",         
        )

        # WHEN
        result = dao.add_attack(fake_attack)

        # THEN 
        assert result


    def test_update_attack(self):
    # GIVEN 
        dao = AttackDao()
        fake_attack = PhysicalFormulaAttack(   
            power=50,
            name = "test",
            description = "testtt" , 
            accuracy=10,
            element="foudre",         
        )

        # WHEN
        result = dao.update_attack(fake_attack)

        # THEN 
        assert result


 

