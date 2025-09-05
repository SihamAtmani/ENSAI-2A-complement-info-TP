from business_object.pokemon.abstract_pokemon import AbstractPokemon

class AllRounderPokemon(AbstractPokemon):
    def __init__(self, stat_current, stat_max=None, level=1, name="", type_pk=None):
        super().__init__(stat_max=stat_max, stat_current=stat_current, level=level, name=name)
       
    def get_pokemon_attack_coef(self) -> float:
            """
            Compute a damage multiplier related to the pokemon type.

            Returns :
                float : the multiplier
            """
            return 1 + (self.sp_atk_current + self.sp_def_current) / 200