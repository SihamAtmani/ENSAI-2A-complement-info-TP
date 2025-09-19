from typing import List, Optional
from dao.type_attack_dao import TypeAttackDAO
from utils.singleton import Singleton
from dao.db_connection import DBConnection
from business_object.attack.abstract_attack import AbstractAttack
from business_object.attack.attack_factory import AttackFactory


class AttackDao(metaclass=Singleton):
    def find_attack_by_id(self,id:int):
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT *                    "
                    "FROM tp.attack AS a " 
                    "JOIN tp.attack_type USING (id_attack_type)"        
                    "WHERE a.id_attack = %(id)s ",
                    {"id": id}
                )
                res = cursor.fetchone()

        attack =  None
        attack_factory = AttackFactory()

        if res:
            attack = attack_factory.instantiate_attack(
                type=res["attack_type_name"], 
                id = res["id_attack"],
                power = res["power"]
            )
        
            return attack
        else:
            return None

    
    def find_all_attacks(self, limit= None, offset = None):
        """
        Retourne la liste de toutes les attaques (optionnellement avec limit et offset).
        """
        request = (
            "SELECT * "
            "FROM tp.attack AS a "
            "JOIN tp.attack_type USING (id_attack_type) "
        )

        # Bonus : ajout de LIMIT / OFFSET si précisé
        if limit is not None:
            request += " LIMIT %(limit)s"
        if offset is not None:
            request += " OFFSET %(offset)s"

        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(request, {"limit": limit, "offset": offset})
                res = cursor.fetchall()

        attacks = []
        attack_factory = AttackFactory()
        for row in res:
            attack = attack_factory.instantiate_attack(
                type=row["attack_type_name"],
                id=row["id_attack"],
                power=row["power"]
            )
            attacks.append(attack)

        return attacks

    def update_attack(self, attack: AbstractAttack) -> bool:
        """
        Met à jour une attaque passée en paramètre.
        Retourne True si la modification a réussi, sinon False.
        """
        requete = (
            "UPDATE tp.attack "
            "SET power = %(power)s, id_attack_type = %(id_attack_type)s "
            "WHERE id_attack = %(id_attack)s"
        )

        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    requete,
                    {
                        "power": attack.power,
                        "id_attack_type": attack.id_attack_type,
                        "id_attack": attack.id
                    }
                )
                updated_rows = cursor.rowcount

        return updated_rows > 0

    def add_attack(self, attack: AbstractAttack) -> bool:
        """
        Add an attack to the database
        """
        created = False

        # Get the id type
        id_attack_type = TypeAttackDAO().find_id_by_label(attack.type)
        if id_attack_type is None:
            return created

        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO tp.attack (id_attack_type, attack_name,        "
                    " power, accuracy, element, attack_description)             "
                    "VALUES                                                     "
                    "(%(id_attack_type)s, %(name)s, %(power)s, %(accuracy)s,    "
                    " %(element)s, %(description)s)                             "
                    "RETURNING id_attack;",
                    {
                        "id_attack_type": id_attack_type,
                        "name": attack.name,
                        "power": attack.power,
                        "accuracy": attack.accuracy,
                        "element": attack.element,
                        "description": attack.description,
                    },
                )
                res = cursor.fetchone()
        if res:
            attack.id = res["id_attack"]
            created = True

        return created




if __name__ == "__main__":
    # Pour charger les variables d'environnement contenues dans le fichier .env
    import dotenv
    from business_object.attack.physical_attack import PhysicalFormulaAttack

    dotenv.load_dotenv(override=True)

    # Création d'une attaque et ajout en BDD
    
    """
    mon_attaque = PhysicalFormulaAttack(
        power=50,
        name="chatouille",
        description="guili-guilis",
        accuracy=90,
        element="Normal",
    )
    
    """

    # succes = AttackDao().add_attack(mon_attaque)
    # print("Attack created in database : " + str(succes))

    id = 3
    recherche_par_id= AttackDao().find_attack_by_id(id)
    print(recherche_par_id)

    print(AttackDao().find_all_attacks())

    print(AttackDao().update_attack())
