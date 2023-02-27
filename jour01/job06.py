class Animal:
    def __init__(self):
        # Attributs age et prenom, age = 0
        self.age = 0
        # Prénom initialisé vide dans le constructeur
        self.prenom = None
        # Print l'age de l'animal
        print("L'age de l'animal", self.age, 'ans')

    # Viellir l'animal de 1 an
    def viellir(self):
        self.age += 1
        print("L'age de l'animal", self.age, 'ans')

    # Nommer l'animal
    def nommer(self, prenom):
        self.prenom = prenom
        print("L'animal se nomme", prenom)

# animal1 = Instance de Animal
animal1 = Animal()

# Viellir l'animal de 1 an
animal1.viellir()

# Nommer l'animal
animal1.nommer('Garfield')