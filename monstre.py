import random
# création de la classe monstre

class Monster:
    def __init__(self, pseudo, pv, force, armure):
        self.pseudo = pseudo
        self.pv = pv
        self.force = force
        self.armure = armure


#function
def generate_monster (pseudo, pv, force, armure):
    monster_object = Monster(pseudo, pv, force, armure)
    dictionnairy = {
        "Pseudo": monster_object.pseudo,
        "PV": monster_object.pv,
        "Force": monster_object.force,
        "Armure": monster_object.armure
    }
#    return print(personnage.pseudo, personnage.pv, personnage.force, personnage.armure)
    return print(dictionnairy)

#excecution
generate_monster("Vespoid", random.randint(5,20), random.randint(3,8), random.randint(0,5))
