from business_object.pokemon.abstract_pokemon import AbstractPokemon

class DefenderPokemon(AbstractPokemon):
    def __init__(self, stat_current, stat_max=None, level=1, name="", type_pk=None):
        super().__init__(
            stat_max=stat_max,
            stat_current=stat_current,
            level=level,
            name=name,
            type_pk=type_pk,
        )

    def get_pokemon_attack_coef(self) -> float:
        sc = self._stat_current 
        return 1 + (sc.attack + sc.defense) / 200
