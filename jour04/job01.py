class Personne:
    def __init__(self, age=14):
        self.age = age

    def afficherAge(self):
        print(self.age)

    def bonjour(self):
        print('Hello')

    def modifierAge(self, nombre):
        self.age = nombre

class Eleve(Personne):
    def __init__(self, age=14):
        super().__init__(age)

    def allerEnCours(self):
        print('Je vais en cours')

    def affichageAge(self):
        print("J'ai", self.age, 'ans')

class Professeur(Personne):
    def __init__(self, matiereEnseignée):
        self.matiereEnseignée = matiereEnseignée

    def enseigner(self):
        print('Le cours va commencer')

    def affichageAge(self):
        print("J'ai", self.age, 'ans')
        
personne1 = Personne()

eleve1 = Eleve()

eleve1.affichageAge()