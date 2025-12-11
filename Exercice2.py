# exerice de classe 2
#Par Milan Mallak

import random
import names

valeur = int
opt_genre = ["male", "female"]
genre = str
rndm_name = str

rndm_profession = str

opt_profession = {
opt_profession["Carpente"] =        [11, 11, 0, 0, 0, 0]
opt_profession["Stonemason"] =      [11, 11, 0, 0, 0, 0]
opt_profession["Armorer"] =         [14, 12, 0, 0, 0, 0]
opt_profession["Blacksmith"] =      [14, 11, 0, 0, 0, 0]
opt_profession["Farmer"] =          [0, 11, 0, 0, 0]
opt_profession["Fisherman"] =       [10, 0, 10, 0, 0, 0]
opt_profession["Miller"] =          [12, 0, 10, 0, 0, 0]
opt_profession["Butcher"] =         [14, 0, 0, 0, 0, 0]
opt_profession["Baker"] =           [0, 0, 0, 0, 10, 0]
opt_profession["Cook"] =            [0, 14, 14, 0, 10, 0
opt_profession["Beerbrewer"] =      [0, 0, 0, 0, 0, 0]
opt_profession["Innkeeper"] =       [0, 0, 0, 0, 0, 10]
opt_profession["Apothecary"] =      [0, 0, 0, 12, 13, 0]
opt_profession["Barber surgeon"] =  [0, 0, 0, 14, 14, 0]
opt_profession["Shoemaker"] =       [0, 14, 0, 0, 0, 0]
opt_profession["Tailor"] =          [0, 14, 0, 0, 0, 0]
opt_profession["Architect"] =       [0, 0, 0, 14, 0, 0]
opt_profession["Clerk"] =           [0, 0, 0, 11, 0, 0]
opt_profession["Merchant"] =        [0, 0, 0, 12, 0, 14]
opt_profession["Bailiff"] =         [14, 0, 0, 0, 12, 0]
opt_profession["Alchemist"] =       [0, 0, 0, 14, 16, 0]
opt_profession["Astronomer"] =      [0, 0, 0, 16, 14, 0]
opt_profession["Candlemaker"] =     [0, 0, 0, 0, 0, 0]
opt_profession["Scribe"] =          [0, 12, 0, 0, 13, 0]

opt_profession = {}                                         #    strg, dex, con, intel, wis, cha
opt_profession["Carpente"] =        [11, 11, 0, 0, 0, 0]    #    11,    11,   0,     0,   0,   0
opt_profession["Stonemason"] =      [11, 11, 0, 0, 0, 0]    #    11,    11,   0,     0,   0,   0
opt_profession["Armorer"] =         [14, 12, 0, 0, 0, 0]    #    14,    12,   0,     0,   0,   0
opt_profession["Blacksmith"] =      [14, 11, 0, 0, 0, 0]    #    14,    11,   0,     0,   0,   0
opt_profession["Farmer"] =          [0, 11, 0, 0, 0]        #    11,     0,  11,     0,   0,   0
opt_profession["Fisherman"] =       [10, 0, 10, 0, 0, 0]    #    10,     0,  10,     0,   0,   0
opt_profession["Miller"] =          [12, 0, 10, 0, 0, 0]    #    12,     0,  10,     0,   0,   0
opt_profession["Butcher"] =         [14, 0, 0, 0, 0, 0]     #    14,     0,   0,     0,   0,   0
opt_profession["Baker"] =           [0, 0, 0, 0, 10, 0]     #     0,     0,   0,     0,  10,   0
opt_profession["Cook"] =            [0, 14, 14, 0, 10, 0]   #     0,    14,  14,     0,  10,   0
opt_profession["Beerbrewer"] =      [0, 0, 0, 0, 0, 0]      #     0,     0,   0,     0,   0,   0
opt_profession["Innkeeper"] =       [0, 0, 0, 0, 0, 10]     #     0,     0,   0,     0,   0,  10
opt_profession["Apothecary"] =      [0, 0, 0, 12, 13, 0]    #     0,     0,   0,    12,  13,   0
opt_profession["Barber surgeon"] =  [0, 0, 0, 14, 14, 0]    #     0,     0,   0,    14,  14,   0
opt_profession["Shoemaker"] =       [0, 14, 0, 0, 0, 0]     #     0,    14,   0,     0,   0,   0
opt_profession["Tailor"] =          [0, 14, 0, 0, 0, 0]     #     0,    14,   0,     0,   0,   0
opt_profession["Architect"] =       [0, 0, 0, 14, 0, 0]     #     0,     0,   0,    14,   0,   0
opt_profession["Clerk"] =           [0, 0, 0, 11, 0, 0]     #     0,     0,   0,    11,   0,   0
opt_profession["Merchant"] =        [0, 0, 0, 12, 0, 14]    #     0,     0,   0,    12,   0,  14
opt_profession["Bailiff"] =         [14, 0, 0, 0, 12, 0]    #    14,     0,   0,     0,  12,   0
opt_profession["Alchemist"] =       [0, 0, 0, 14, 16, 0]    #     0,     0,   0,    14,  16,   0
opt_profession["Astronomer"] =      [0, 0, 0, 16, 14, 0]    #     0,     0,   0,    16,  14,   0
opt_profession["Candlemaker"] =     [0, 0, 0, 0, 0, 0]      #     0,     0,   0,     0,   0,   0
opt_profession["Scribe"] =          [0, 12, 0, 0, 13, 0]    #     0,    12,   0,     0,  13,   0

def ctrl_rndm_profession():




def rndm_attribut():
    global valeur
    ld = []
    for a in range(4):
        ld.append(random.randint(1, 6)) # lancé de dés 6
    ld.sort(reverse = True)
    valeur = ld[0] + ld[1] + ld[2] # les trois meilleurs

def rndm_caracteristics():
    global rndm_name

    if genre == "male" :
        rndm_first_name = names.get_first_name(gender = "male")
    else :
        rndm_first_name = names.get_first_name(gender="female")

    rndm_last_name = names.get_last_name()
    rndm_name = rndm_first_name + " " + rndm_last_name
    return rndm_name

class NPC :
    def __init__(self, strg, dex, con, intel, wis, cha, nom):
        self.strg = strg
        self.dex = dex
        self.con = con
        self.intel = intel
        self.wis = wis
        self.cha = cha

        self.HP = random.randint(1, 20) # dé 20
        self.ac = random.randint(1, 12) # dé 12

        self.genre = random.choice(opt_genre)
        self.nom = nom

        #self.species = placeholder
        #self.ethnicity = placeholder

        #self.profession = placeholder

rndm_attribut()
NPC.strg = valeur
rndm_attribut()
NPC.dex = valeur
rndm_attribut()
NPC.con = valeur
rndm_attribut()
NPC.intel = valeur
rndm_attribut()
NPC.wis = valeur
rndm_attribut()
NPC.cha = valeur

NPC.nom = rndm_caracteristics()

print(NPC.strg, NPC.dex, NPC.con, NPC.intel, NPC.wis, NPC.cha, NPC.nom)