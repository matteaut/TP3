# Tristan Matteau - TP3

import random

def main():
    vie = 20
    victoire = 0
    defaite = 0
    victoire_consecutive = 0
    while vie >= 1:

        result_dice1 = random.randint(1, 6)
        result_dice2 = random.randint(1, 6)

        combined_dice = result_dice1 + result_dice2

        force_de_monstre = random.randint(1, 7)

        print("Un monstre de force",force_de_monstre,"est apparue!")
        print("Tu as %d vies!!!"%vie)
        print("Choissez entre:\nTe battre contre le monstre - 1\nContourner le monstre - 2\nAfficher les règles - 3\nQuitter la partie - 4")

        selectionporte = int(input("Entrez votre choix: "))
        print("\n\n\n-------------------\n\n\n")
        if selectionporte == 1: #Combat

            print("Votre attaque apres avoir tourner les dé est", result_dice1, "+", result_dice2,"donc votre attaque est", combined_dice)

            if combined_dice > force_de_monstre: #Gagner le combat
                print("victoire!!!, \nVotre vie a augmenté")
                vie += force_de_monstre
                victoire += 1
            elif combined_dice <= force_de_monstre: #Perdre le combat

                print("defaite")
                defaite += 1

            print(victoire, "vs", defaite)

        elif selectionporte == 2: #Contourner

            print("Votre vie a diminuer")
            vie -= 1

        elif selectionporte == 3: #Afficher les règles

            pass

        else: #Quitter la partie


            vie = 0

main()
print("Bye!")
