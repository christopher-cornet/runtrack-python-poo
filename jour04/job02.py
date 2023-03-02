class Personne:
    def __init__(self, age):
        self.age = age

    def afficherAge(self):
        print(self.age)

    def bonjour(self):
        print('Hello')

    def modifierAge(self, nombre):
        self.age = nombre

class Eleve(Personne):
    def __init__(self, age):
        self.age = age

    def allerEnCours(self):
        print('Je vais en cours')

    def affichageAge(self, age):
        print("J'ai", age, 'ans')

class Professeur(Personne):
    def __init__(self, age, matiereEnseignée):
        self.matiereEnseignée = matiereEnseignée

    def enseigner(self):
        print('Le cours va commencer')

    def affichageAge(self):
        print("J'ai", self.age, 'ans')
        
personne1 = Personne(14)

eleve1 = Eleve(18)

eleve1.bonjour()

eleve1.allerEnCours()

eleve1.affichageAge(15)

professeur1 = Professeur(40, 'mathématiques')

professeur1.bonjour()

professeur1.enseigner()