class Personne:
    def __init__(self):
        pass

    def SePresenter(self, nom, prenom):
        print('Je suis', prenom, nom)
        return nom, prenom
    
personne1 = Personne()
personne1.SePresenter('cornet', 'christopher')