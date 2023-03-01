class Ville:
    def __init__(self, nom, nbhabitants):
        self.__nom = nom
        self.__nbhabitants = nbhabitants

    # Prend le nombre d'habitants
    def getHabitants(self):
        return self.__nbhabitants
    
    # Redéfinir le nombre d'habitants
    def setHabitants(self, add):
        self.__nbhabitants = add

class Personne:
    def __init__(self, nom, age, ville):
        self.__nom = nom
        self.__age = age
        self.__ville = ville

    def ajouterPopulation(self, ville):
        # Incrémenter le nombre d'habitants de 1
        new_nbhabitant = ville.getHabitants() + 1
        # Définir le nouveau nombre d'habitants
        ville.setHabitants(new_nbhabitant)

# Ville 1 et Ville 2
ville1 = Ville('Paris', 1000000)
print('Population de la ville de Paris:', ville1.getHabitants(), 'habitants')

ville2 = Ville('Marseille', 861635)
print('Population de la ville de Marseille:', ville2.getHabitants(), 'habitants')

# Personnes
personne1 = Personne('John', 45, ville1)
personne2 = Personne('Myrtille', 4, ville1)
personne3 = Personne('Chloé', 18, ville2)

personne1.ajouterPopulation(ville1)
personne2.ajouterPopulation(ville1)
personne3.ajouterPopulation(ville2)

print('Mise a jour de la population de la ville de Paris:', ville1.getHabitants(), 'habitants')

print('Mise a jour de la population de la ville de Marseille:', ville2.getHabitants(), 'habitants')