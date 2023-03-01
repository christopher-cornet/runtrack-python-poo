class CompteBancaire:
    def __init__(self, numdecompte, prenom, nom, solde):
        self.__numdecompte = numdecompte
        self.__prenom = prenom
        self.__nom = nom
        self.__solde = solde
        self.découvert = True

    # affiche le détail sur le compte
    def afficher(self):
        print('Détails du compte:')
        print('Numéro de compte:', self.__numdecompte)
        print('Prénom:', self.__prenom)
        print('Nom:', self.__nom)
        print('Solde =', self.__solde)
    
    # affiche le solde du client
    def afficherSolde(self):
        print('Solde du compte:', self.__solde)

    # prend un paramètre le montant du versement et ajoute celui-ci au solde du client
    def versement(self, montant):
        self.__solde += montant

    # prend un entier en argument (le montant à retirer) et
    # enlever ce montant au solde du compte et afficher le nouveau solde.
    def retrait(self, montant):
        # Si solde du compte supérieur au montant à retirer ou si le découvert est autorisé,
        # retire le montant du solde du compte, sinon print une erreur
        if self.__solde >= montant or self.découvert == True:
            self.__solde -= montant # retire un montant du solde
            self.__solde -= self.agios() # retire les agios du solde
        else:
            print('Erreur, le solde du compte est inférieur au montant.')

    def agios(self):
        self.__solde = self.__solde * 7 # jours
        self.__solde = self.__solde * 0.15 # multiplier par le taux d'intéret 15 %
        result = self.__solde / 365 # divise par le nombre de jour dans l'année
        self.__solde = result # définit le solde en résultat
        result = round(self.__solde, 2) # arrondit à 2 décimales (pas demandé dans le sujet)
        return result
    
    def virement(self, compte1, compte2, montant):
        if compte1.__solde >= montant or compte1.découvert:
            compte1.__solde -= montant
            compte2.__solde += montant
            print('Virement effectué. Solde de', compte2.__prenom, compte2.__nom, '+', montant)
            print('Solde de', compte2.__prenom, compte2.__nom, '=', compte2.__solde)
        else:
            print('Erreur, le virement ne peut être effectué.')
        
compte1 = CompteBancaire(1, 'Jeff', 'Bezos', 100)

compte1.afficher()

compte1.afficherSolde()

compte1.retrait(200)

compte1.agios()

compte2 = CompteBancaire(2, 'Elon', 'Musk', -100)

compte2.afficherSolde()

compte1.virement(compte1, compte2, 200)