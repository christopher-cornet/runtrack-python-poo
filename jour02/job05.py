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

car = Voiture('Tesla', 'Model X', 2016, 40000, 50)

car.demarrer()