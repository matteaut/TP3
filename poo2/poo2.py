#Cree par Tristan Matteau
#POO 2 + 3


import random


def des():
    des1 = random.randint(1, 6)
    des2 = random.randint(1, 6)
    des3 = random.randint(1, 6)
    des4 = random.randint(1, 6)
    ran = [des1, des2, des3, des4]
    ran.remove(min(ran))
    sum(ran)
    return(ran)

def attribut():
    des1 = random.randint(1, 6)
    des2 = random.randint(1, 6)
    des3 = random.randint(1, 6)
    des4 = random.randint(1, 6)
    ran = [des1, des2, des3, des4]
    ran.remove(min(ran))
    return(ran)


class NPC:
    def __init__(self):
        self.Force = des()
        self.Agilite = des()
        self.Constitiution = des()
        self.Intelligence = des()
        self.Sagesse = des()
        self.Charisme = des()
        self.classearmure = random.randint(1, 12)
        self.nom = None
        self.race = None
        self.espece = None
        self.pointdevie = random.randint(1, 20)
        self.profession = None

    def caracteristiques(self):
        print("Force =", self.Force)
        print("Agilité =", self.Agilite)
        print("Constitiution =", self.Constitiution )
        print("Intelligence =", self.Intelligence )
        print("Sagesse =", self.Sagesse)
        print("Charisme =", self.Charisme)
        print("Class armure =", self.classearmure)
        print("Nom =", self.nom)
        print("Espèce =", self.espece)
        print("Point de vie =", self.pointdevie)
        print("Profession =", self.profession)


class  kobold(NPC):

    def __init__(self):
        super().__init__()
        self.race = "Kobold"
        self.espece = "Monstre"
        self.profession = "mercenaire"

class Heros(NPC):
    def __init__(self):
        super().__init__()
        self.race = "blanc"
        self.espece = "humain"
        self.profession = "Héros"
        self.nom = "Moi"