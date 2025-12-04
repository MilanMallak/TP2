# exerice de classe 2
#Par Milan Mallak

import random
import names

valeur = int
opt_genre = ["male", "female"]
genre = str
opt_profession = [""]
rndm_name = str

# Carpenter : 11-strg 11-dex
# Stonemason : 11-strg 11-dex

# Armorer : 14-strg 12-dex
# Blacksmith : 14-strg 11-dex

# Farmer : 10-stg 11-con
# Fisherman : 10-stg 11-con
# Miller : 12-stg 10-con

# Butcher : 14-str
# Baker : 10-wis
# Cook : 14-dex 14-con 10-wis
# Beerbrewer : no req
# Innkeeper : 10-cha

# Apothecary : 12-intel 13-wis
# Barber surgeon : 14-intel 14-wis

# Shoemaker : 14-dex
# Tailor : 14-dex

# Architect : 14-intel

# Clerk : 11-intel
# Merchant : 12-intel 14-cha
# Bailiff : 14-strg 12-wis

# Alchemist : 14-int 16 wis
# Astronomer : 16-intel 14-wis

# Candlemaker : no req
# Scribe : 12-dex 13-wis

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