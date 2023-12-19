#Cree par Tristan Matteau

import random

def des():
    des1 = random.randint(1, 6)
    des2 = random.randint(1, 6)
    des3 = random.randint(1, 6)
    des4 = random.randint(1, 6)
    totaldes = [des1, des2, des3, des4]
    totaldes.remove(min(des1, des2, des3, des4))


class NPC():
    def __init__(self):
        self.force = des()
        self.agilite = des()
        self.constitution = des()
        self.intelligence = des()
        self.sagesse = des()
        self.charisme = des()

        self.armure = random.randint(1, 12)
        self.nom = None
        self.race = None
        self.espece = None
        self.hp = random.randint(1, 20)

    def __afficher_caracteristiques__(self):
        print("Force : ", self.force)
        print("Agilité : ", self.agilite)
        print("Constitution : ", self.constitution)
        print("Intelligence : ", self.intelligence)
        print("Sagesse : ", self.sagesse)
        print("Charisme : ", self.charisme)
        print("Armure : ", self.armure)
        print("Nom : ", self.nom)
        print("Race : ", self.race)
        print("Espèce : ", self.espece)
        print("HP : ", self.hp)





ag