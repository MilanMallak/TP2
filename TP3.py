#ce code est un jeu ou le but est de battre plus d'adversaire possible dans un donjon
#Par Milan Mallak

import random
niveau_vie = 20
force_adversaire = type[int]
wins = 0
Boss = False

def fight():
    global niveau_vie
    global force_adversaire
    global wins
    global Boss

    if Boss == False :
        Dice_throw = random.randint(1, 6)
        if Dice_throw >= force_adversaire :
            niveau_vie += force_adversaire
            wins += 1
            print(f"""Bravo, vous avez gagner se combat
            Vous avez maintenant {niveau_vie} points de vie et {wins} victoires.""")
            if wins % 3 == 0 :
                Boss = True
        else :
            niveau_vie -= force_adversaire
            print(f"""Malhereusement, vous avez perdue se combat
            Vous avez maintenant {niveau_vie} points de vie.""")
    else :
        Dice_throw = random.randint(1, 6)
        if Dice_throw >= force_adversaire :
            niveau_vie += force_adversaire
            wins += 1
            print(f"""Bravo, vous avez vaincu le boss!
            Vous avez maintenant {niveau_vie} points de vie et {wins} victoires.""")
        else :
            niveau_vie -= force_adversaire
            print(f"""Malhereusement, vous avez perdue le combat
            Vous avez maintenant {niveau_vie} points de vie.""")
        Boss = False


def avoid():
    global niveau_vie

    print("Vous éviter le combat et perdez 1 point de vie.")
    niveau_vie -= 1
    print(f"Vous avez maintenant {niveau_vie} points de vie")


def new_room():
    global niveau_vie
    global force_adversaire
    global wins
    global Boss

    if niveau_vie <= 0 :
        print(f"""Vous êtes succombez à vos blessures,
        vous aviez {wins} victoires, félicitation.""")
        exit()

    print(f"""Vous avez {wins} victoires et {niveau_vie} de vie""")
    if Boss == True :
        force_adversaire = random.randint(5, 6)
        print(f"Vous tombez face à face avec un boss de difficulté {force_adversaire} !")
    else :
        force_adversaire = random.randint(1, 5)
        print(f"Vous tombez face à face avec un adversaire de difficulté {force_adversaire}")

    def action():
        choice = int(input("""Que voulez-vous faire ?
            1- Combattre cet adversaire
            2- Contourner cet adversaire et aller ouvrir une autre porte
            3- Afficher les règles du jeu
            4- Quitter la partie"""))  # options d'actions

        if choice == 1:
            fight()
            new_room()
        elif choice == 2:
            avoid()
            new_room()
        elif choice == 3:
            print("""Vous commencez la partie avec une niveau de vie de 20
            Vous vous retrouvez face à face avec un adversaire d'une force de 1 à 5
            Vous pouvez soit combattre cet adversaire ou contourner cet adversaire et aller ouvrir une autre porte
            Si vous attaquer l'adversaire le jeu effectueras un lancer de dé (dé six), 
            le résultat doit être plus haut que la force du monstre pour que vous gagnier

            Dans eventualité que vous gangner, vous gagnerez en nombres de vie la force de l'ennemi que vous avez vaincu.
            Cependant, si vous perdez, vous perderez en le nombres de vie la force de l'ennemi qui vous a vaincu.

            Si vous décidez de contourner cet adversaire il y aura une pénalité de 1 point de vie, 
            ensuite, vous vous retrouverez contre un nouvelle adversaire.

            Le but du jeu est d'accumuler le plus de victoires.""")  # règles
            action()
        else:
            print(f"Vous aviez {wins} victoires, félicitation.")
            exit()

    action()

new_room()