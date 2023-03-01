class Voiture:
    def __init__(self, marque, modèle, année, kilométrage, reservoir):
        self.__marque = marque
        self.__modèle = modèle
        self.__année = année
        self.__kilométrage = kilométrage
        self.en_marche = False
        self.__reservoir = reservoir

    def demarrer(self):
        self.en_marche = True
        if self.__verifier_plein() > 5:
            print('La voiture peut démarrer.')

    def arreter(self):
        self.en_marche = False

    def __verifier_plein(self):
        return self.__reservoir
    
    # Get
    def getmarque(self):
        return self.__marque
    
    def getmodele(self):
        return self.__modèle
    
    def getannee(self):
        return self.__année
    
    def getkilometrage(self):
        return self.__kilométrage
    
    # Set
    def setmarque(self, marque):
        self.__marque = marque

    def setmodele(self, modele):
        self.__modèle = modele
    
    def setannee(self, annee):
        self.__année = annee
    
    def setkilometrage(self, km):
        self.__kilométrage = km

car = Voiture('Tesla', 'Model X', 2016, 43874, 50)

car.demarrer()

# Get
print(car.getmarque())
print(car.getmodele())
print(car.getannee())
print(car.getkilometrage())

# Set
car.setmarque('Koenigsegg')
car.setmodele('Gemera')
car.setannee(2021)
car.setkilometrage(55348)

print('Modification:')

# Modif
print(car.getmarque())
print(car.getmodele())
print(car.getannee())
print(car.getkilometrage())