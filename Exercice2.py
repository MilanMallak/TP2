# exerice de classe 2
#Par Milan Mallak

import random
import names

valeur = int
opt_genre = ["male", "female"]
genre = str
rndm_name = str
opt_profession = [""]
rndm_profession = str

prf_strg = []


def ctrl_rndm_profession():




#                                       strg, dex, con, intel, wis, cha
# Carpenter : 11-strg 11-dex :          11,    11,   0,     0,   0,   0
# Stonemason : 11-strg 11-dex :         11,    11,   0,     0,   0,   0

# Armorer : 14-strg 12-dex :            14,    12,   0,     0,   0,   0
# Blacksmith : 14-strg 11-dex :         14,    11,   0,     0,   0,   0

# Farmer : 10-stg 11-con :              11,     0,  11,     0,   0,   0
# Fisherman : 10-stg 11-con :           10,     0,  10,     0,   0,   0
# Miller : 12-stg 10-con :              12,     0,  10,     0,   0,   0

# Butcher : 14-str :                    14,     0,   0,     0,   0,   0
# Baker : 10-wis :                       0,     0,   0,     0,  10,   0
# Cook : 14-dex 14-con 10-wis :          0,    14,  14,     0,  10,   0
# Beerbrewer : no req :                  0,     0,   0,     0,   0,   0
# Innkeeper : 10-cha :                   0,     0,   0,     0,   0,  10

# Apothecary : 12-intel 13-wis :         0,     0,   0,    12,  13,   0
# Barber surgeon : 14-intel 14-wis :     0,     0,   0,    14,  14,   0

# Shoemaker : 14-dex :                   0,    14,   0,     0,   0,   0
# Tailor : 14-dex :                      0,    14,   0,     0,   0,   0

# Architect : 14-intel :                 0,     0,   0,    14,   0,   0

# Clerk : 11-intel :                     0,     0,   0,    11,   0,   0
# Merchant : 12-intel 14-cha :           0,     0,   0,    12,   0,  14
# Bailiff : 14-strg 12-wis :            14,     0,   0,     0,  12,   0

# Alchemist : 14-int 16 wis :            0,     0,   0,    14,  16,   0
# Astronomer : 16-intel 14-wis :         0,     0,   0,    16,  14,   0

# Candlemaker : no req :                 0,     0,   0,     0,   0,   0
# Scribe : 12-dex 13-wis :               0,    12,   0,     0,  13,   0

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