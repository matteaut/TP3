# Tristan Matteau - TP3

import random


def regle():
    print("Pour réussir un combat, il faut que la valeur du dé lancé soit supérieure à la force de l’adversaire.  Dans ce cas, le niveau de vie de l’usager est augmenté de la force de l’adversaire.\nUne défaite a lieu lorsque la valeur du dé lancé par l’usager est inférieure ou égale à la force de l’adversaire.  Dans ce cas, le niveau de vie de l’usager est diminué de la force de l’adversaire.\nLa partie se termine lorsque les points de vie de l’usager tombent sous 0. \n L’usager peut combattre ou éviter chaque adversaire, dans le cas de l’évitement, il y a une pénalité de 1 point de vie.")

def main():
    vie = 20
    victoire = 0
    defaite = 0
    victoire_consecutive = 0
    force_du_boss = 10


    while vie >= 1:

        result_dice1 = random.randint(1, 6)
        result_dice2 = random.randint(1, 6)

        combined_dice = result_dice1 + result_dice2

        force_de_monstre = random.randint(1, 7)

        if victoire_consecutive == 3:
            print("boss est apparue")
            print("Le Boss à une force de", force_du_boss, "!")
            print("Votre attaque apres avoir tourner les dé est", result_dice1, "+", result_dice2,
                  "donc votre attaque est", combined_dice)

            if combined_dice > force_du_boss:  # Gagner le combat
                print("victoire!!!, \nVotre vie a augmenté")
                vie += force_du_boss
                victoire += 1
                victoire_consecutive += 1
            elif combined_dice <= force_du_boss:  # Perdre le combat

                print("defaite")
                defaite += 1
                victoire_consecutive = 0

            print(victoire, "vs", defaite)


        print("Un monstre est apparue!")
        print("Tu as %d vies!!!"%vie)
        print("Vous devez choisir entre:\nTe battre contre le monstre - 1\nContourner le monstre - 2\nAfficher les règles - 3\nQuitter la partie - 4")

        selectionporte = int(input("Entrez votre choix: "))
        print("\n\n\n-------------------\n\n\n")
        if selectionporte == 1: #Combat

            print("Le monstre à une force de", force_de_monstre, "!")
            print("Votre attaque apres avoir tourner les dé est", result_dice1, "+", result_dice2,"donc votre attaque est", combined_dice)

            if combined_dice > force_de_monstre: #Gagner le combat
                print("victoire!!!, \nVotre vie a augmenté")
                vie += force_de_monstre
                victoire += 1
                victoire_consecutive += 1
            elif combined_dice <= force_de_monstre: #Perdre le combat

                print("defaite")
                defaite += 1
                victoire_consecutive = 0

            print(victoire, "vs", defaite)

        elif selectionporte == 2: #Contourner

            print("Votre vie a diminuer")
            vie -= 1

        elif selectionporte == 3: #Afficher les règles
            regle()


        else: #Quitter la partie


            vie = 0


main()
print("Bye!")
