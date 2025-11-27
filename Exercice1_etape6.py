# exerice de classe 1, étape 6
#Par Milan Mallak

import random

class Hero :
    def __init__(self, nb_pt_vie, force_atk, force_def, nom, strg, dex, con, intel, wis, cha):
        self.nb_pt_vie = nb_pt_vie
        self.force_atk = force_atk
        self.force_def = force_def
        self.nom = nom

        self.strg = strg
        self.dex = dex
        self.con = con
        self.intel = intel
        self.wis = wis
        self.cha = cha
    def attaque(self, dmg_inflige):
        dmg_inflige = random.randint(1, 6) + (self.force_atk // 4)
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

Hero.strg = random.randint(1, 20)
Hero.dex = random.randint(1,20)
Hero.con = random.randint(1, 20)
Hero.intel = random.randint(1, 20)
Hero.wis = random.randint(1, 20)
Hero.cha = random.randint(1, 20)

Hero.force_atk = Hero.strg
Hero.force_def = Hero.con
Hero.nb_pt_vie = 10 + (Hero.con // 2)

print(f"""Vous avez
{Hero.strg} en force,
{Hero.dex} en dextérité,
{Hero.con} en constitution,
{Hero.intel} en intelligence,
{Hero.wis} en sagesse et 
{Hero.cha} en charisme.

Vos points de vies sont de {Hero.nb_pt_vie}.""")

Hero.nom = input("Quelle est votre nom?")

