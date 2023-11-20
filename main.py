# Tristan Matteau
# TP3

import random

result_dice1 = random.randint(1, 6)
result_dice2 = random.randint(1, 6)

combined_dice = result_dice1 + result_dice2

vie = 20





def victoires():
    victoires == 0
    if combat1 == victoires:
        victoires+1

    else:
        victoires+0

def force_de_base():
    force_de_base == 2

def defaite():
    defaite == 0
    defaite + 1


def victoire():
    victoire == 0
    victoire + 1

def nombre_de_defaite():
    print("nombre_de_defaite")

def nombre_de_victoire():
    print("nombre_de_victoire")

def numero_de_combat():
    print("nombre_de_victoire vs nombre_de_defaite")

def force_de_monstre1():
    force_de_monstre1 == random.randint(1, 5)

def monstre1():
    monstre1 == force_de_monstre1

def force_de_monstre2():
    force_de_monstre2 == random.randint(3, 7)

def monstre2():
    monstre2 == force_de_monstre2

def force_de_monstre3():
    force_de_monstre3 == random.randint(5, 11)

def monstre3():
    monstre3 == force_de_monstre3



def SelectionPorte():
    print("choissez entre porte1 , porte2 , porte3 .")
    SelectionPorte == str(input("Entrez votre choix de porte: "))

def combat1():
    print("Le monstre de force" ,force_de_monstre1, "vous attaque ")
    print("adversaire de difficulter de force " ,force_de_monstre1, "est apparue. \n Il vous attaque. \n Votre attaque apres avoir tourner les dé est", result_dice1 ,"+",result_dice2,"donc votre attaque est", combined_dice)

    if force_de_base + combined_dice > force_de_monstre1:
        print("victoire")
        print(nombre_de_victoire)

    else:
        force_de_base + combined_dice < force_de_monstre1
        print("defaite")
        print(nombre_de_defaite)


def combat2():
    print("Le monstre de force", force_de_monstre2, "vous attaque ")
    print("adversaire de difficulter de force ", force_de_monstre2,
          "est apparue. \n Il vous attaque. \n Votre attaque apres avoir tourner les dé est", result_dice1, "+",
          result_dice2, "donc votre attaque est", combined_dice)

    if force_de_base + combined_dice > force_de_monstre2:
        print("victoire")
        print(nombre_de_victoire)

    else:
        force_de_base + combined_dice < force_de_monstre2
        print("defaite")
        print(nombre_de_defaite)


def combat3():
    print("Le monstre de force", force_de_monstre3, "vous attaque ")
    print("adversaire de difficulter de force ", force_de_monstre3,
          "est apparue. \n Il vous attaque. \n Votre attaque apres avoir tourner les dé est", result_dice1, "+",
          result_dice2, "donc votre attaque est", combined_dice)

    if force_de_base + combined_dice > force_de_monstre3:
        print("victoire")
        print(nombre_de_victoire)

    else:
        force_de_base + combined_dice < force_de_monstre3
        print("defaite")
        print(nombre_de_defaite)

def porte1():
    porte1 == random.choice(porte11, porte22, porte33)
def porte2():
    porte2 == random.choice(porte11, porte22, porte33)
def porte3():
    porte3 == random.choice(porte11, porte22, porte33)
def porte11():
    porte11 == random.choice(monstre1, monstre2, monstre3)
    if porte11 == monstre1:
        print("un monstre de force",force_de_monstre1,"est apparue!")
        combat1()

    elif porte11 == monstre2:
        print("un monstre de force", force_de_monstre2, "est apparue!")
        combat2()

    else:
        print("un monstre de force", force_de_monstre3, "est apparue!")
        combat3()
def porte22():
    print("votre vie a augmenter")
    vie + 2


def porte33():
    print("votre vie a diminuer")
    vie - 1

SelectionPorte()




