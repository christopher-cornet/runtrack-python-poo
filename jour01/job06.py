class Animal:
    def __init__(self, age):
        self.age = age
        self.prenom = None
        print("L'age de l'animal", age, 'ans')

    def viellir(self, age):
        age += 1
        print("L'age de l'animal", age, 'ans')

    def nommer(self, prenom):
        self.prenom = prenom
        print("L'animal se nomme", prenom)

animal1 = Animal(0)

animal1.viellir(0)

animal1.nommer('Garfield')