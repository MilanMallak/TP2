# exerice de classe 6
#Par Milan Mallak

import random

class Hero :
    def __init__(self, nb_pt_vie, force_atk, force_def, nom):
        self.nb_pt_vie = nb_pt_vie
        self.force_atk = force_atk
        self.force_def = force_def
        self.nom = nom
    def attaque(self, dmg_inflige):
        dmg_inflige = random.randint(1, 6) + self.force_atk
    def recevoir_dmg(self, dmg_recu):
        if dmg_recu <= self.force_def :
            print("Vous avez pris aucun dégats")
        else:
            self.nb_pt_vie -= dmg_recu - self.force_def
            print(f"""Vous avez pris {dmg_recu} dégats.
            Vous avez maintenant {self.nb_pt_vie} points de vie.""")
    def life_check(self):
        if self.nb_pt_vie <= 0 :
            print("Vous avez succombé à vos blessures.")

