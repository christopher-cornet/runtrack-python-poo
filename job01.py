class Rectangle:
    def __init__(self, longueur, largeur):
        # Longueur et largeur en attribut
        self.__longueur = longueur
        self.__largeur = largeur

    def getrect(self):
        # Getrect valeur = longueur et largeur
        return self.__longueur, self.__largeur

    def setrect(self):
        # Modif longueur et largeur
        self.__longueur = 20
        self.__largeur = 10
        return self.__longueur, self.__largeur

rect = Rectangle(10, 5)
print(rect.getrect())

print(rect.setrect())