class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def périmètre(self):
        # (L + l) * 2
        somme = self.__longueur + self.__largeur
        return somme * 2

    def surface(self):
        # Longueur * largeur
        somme = self.__longueur * self.__largeur
        return somme

class Parallélépipède(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)
        self.hauteur = hauteur

    def getvolume(self):
        return self.__longueur, self.__largeur, self.hauteur

    def volume(self):
        # multiplier longueur, largeur, hauteur
        somme = self.__longueur * self.__largeur * self.hauteur
        return somme

rect = Rectangle(5, 10)

print('Périmètre:', rect.périmètre())

print('Surface:', rect.surface())

print('Volume:', Parallélépipède.volume())