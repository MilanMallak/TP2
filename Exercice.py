#ce code
#Par Milan Mallak


from math import pi

# exercice de classe 1
class StringFoo :
    def __init__(self, message):
        self.message = message
    def set_string(self):
        self.message = input("Message:")
    def print_string(self):
        print(self.message.upper())

stringfoo = StringFoo("")
stringfoo.set_string()
stringfoo.print_string()

class Rectangle :
    def __init__(self, largeur, longueur, aire_R):
        self.largeur = largeur
        self.longueur = longueur
        self.aire_R = aire_R
    def calcul_aire_R(self):
        self.aire_R = self.largeur * self.longueur
    def afficher_infos_R(self):
        print(f"Aire:{self.aire_R}")

print("Mesures du rectangle")
largeur = int(input("Largeur:"))
longueur = int(input("Longueur:"))
aire_R = int

rectangle = Rectangle(largeur, longueur, aire_R)
rectangle.calcul_aire_R()
rectangle.afficher_infos_R()

class Cercle :
    def __init__(self, rayon, aire_C, circonference):
        self.rayon = rayon
        self.aire_C = aire_C
        self.circonference = circonference
    def calcul_aire_C(self):
        self.aire_C = pi * self.rayon ** 2
    def calcul_circonference_C(self):
        self.circonference = 2 * pi * self.rayon
    def afficher_infos_C(self):
        print(f"Aire:{self.aire_C}")
        print(f"Circonférence:{self.circonference}")

print("Mesures du cercle")
rayon = int(input("Rayons:"))
aire_C = int
circonference = int

cercle = Cercle(rayon, aire_C, circonference)
cercle.calcul_aire_C()
cercle.calcul_circonference_C()
cercle.afficher_infos_C()

class Hero :
    def __init__(self, nb_pt_vie, force_atk, force_def, nom):
        self.nb_pt_vie = nb_pt_vie
        self.force_atk = force_atk
        self.force_def = force_def
        self.nom = nom
    def attaque(self):
