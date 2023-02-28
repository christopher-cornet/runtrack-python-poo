class Commande:
    def __init__(self, numdecommande, platscommandés, statutcommande):
        self.__numdecommande = numdecommande
        self.__platscommandés = platscommandés
        self.__statutcommande = statutcommande

command = Commande()

command()