class Commande1:
    def __init__(self, numdecommande, platscommandés, statutcommande):
        self.__numdecommande = numdecommande
        self.__platscommandés = platscommandés
        self.__statutcommande = statutcommande
        self.plats_dict = {'Sushi': 1, 'Pâtes': 2, 'Poulet du général tao': 3}
        nomplat, prix, statut = 'Nom', 5, 'en cours'
        print(self.plats_dict)

    # Ajouter un plat à la commande
    def ajouter_plat(self):
        pass
    
    # Annuler une commande
    def annuler_commande(self):
        pass

    # Calculer le total d’une commande
    def __calculer_total_commande(self):
        pass

    # Afficher une commande avec son total à payer
    def afficher_commande(self):
        pass

    # Calculer la TVA
    def calculer_TVA(self):
        pass

command1 = Commande1(10, 2, 'en cours')