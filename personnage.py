# from tokenize import PseudoExtras
# from typing_extensions import Self

# création de la classe personnage
class Personnage:
    def __init__(self, pseudo, pv, force, armure):
        self.pseudo = pseudo
        self.pv = pv
        self.force = force
        self.armure = armure


#function
def create_hero (pseudo, pv, force, armure):
    personnage = Personnage(pseudo, pv, force, armure)
    dictionnairy = {
        "Pseudo": personnage.pseudo,
        "PV": personnage.pv,
        "Force": personnage.force,
        "Armure": personnage.armure
    }
#    return print(personnage.pseudo, personnage.pv, personnage.force, personnage.armure)
    return print(dictionnairy)

#excecution
create_hero("aziza", 5, 3, 20)

