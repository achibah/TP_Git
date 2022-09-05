import monstre
import random

def creation_monstre():
   dictionnairy = monstre.generate_monster(input("le nom du monstre est : " ), random.randint(5,20), random.randint(3,8), random.randint(0,5))
   return print(dictionnairy)


creation_monstre()