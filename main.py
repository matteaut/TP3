# Tristan Matteau
# TP3

import random

result_dice1 = random.randint(1, 6)
result_dice2 = random.randint(1, 6)

vie = 20





def victoires():
    victoires == 0
    if combat1==victoires:
        victoires+1

    else:
        victoires+0

def force_de_base():
    force_de_base==2

def nombre_de_victoire():
    print("victoires")

def nombre_de_defaite():
    print("defaites")

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
    force_de_monstre3 == random.randint(5, 15)

def monstre3():
    monstre3 == force_de_monstre3

def debut_du_jeu():
    debut_du_jeu == monstre1


def SelectionPorte():
    print("choissez entre porte1 , porte2 , porte3 .")
    SelectionPorte == int(input("Entrez votre choix de porte: "))

def combat1():
    if force_de_base + result_dice1 + result_dice2 > force_de_monstre1:
        print("Victoires")
        print("Nombre de victoires")

def porte():
    porte == random.choice(porte1, porte2, porte3)

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
        combat()

    elif porte11== monstre2:
        print("un monstre de force", force_de_monstre2, "est apparue!")
        combat()

    else:
        print("un monstre de force", force_de_monstre3, "est apparue!")
        combat()
def porte22():
    print("votre vie a augmenter")
    vie + 2


def porte33():
    print("votre vie a diminuer")
    vie - 1



print("adversaire de difficulter de force " ,force_de_monstre1, "est apparue.")



