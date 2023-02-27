class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = None
        print("L'age de l'animal", self.age, 'ans')

    def viellir(self):
        self.age += 1
        print("L'age de l'animal", self.age, 'ans')

    def nommer(self, prenom):
        self.prenom = prenom
        print("L'animal se nomme", prenom)

animal1 = Animal()

animal1.viellir()

animal1.nommer('Garfield')