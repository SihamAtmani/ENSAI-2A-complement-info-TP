from abstract_pokemon import AbstractPokemon
from business_object.pokemon.abstract_pokemon import AbstractPokemon

class AttackerPokemon(AbstractPokemon):
    def __init__(self):
        super().__init__(stat_max=stat_max, stat_current=stat_current, level=level, name=name)
       
   def get_pokemon_attack_coef(self) -> float:
        """
        Compute a damage multiplier related to the pokemon type.

        Returns :
            float : the multiplier
        """
        return 1 + (self.speed_current + self.attack_current) / 200
       