class Personne:
    def __init__(self, prenom, nom):
        # Attributs prenom et nom
        self.prenom = prenom
        self.nom = nom

    # Méthode pour se présenter
    def SePresenter(self):
        print('Je suis', self.prenom, self.nom)
    
# Valeur des attributs prenom et nom
personne1 = Personne('Christopher', 'Cornet')
# Se présenter
personne1.SePresenter()