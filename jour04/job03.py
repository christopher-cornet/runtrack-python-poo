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
    
    def getlongueur(self):
        return self.__longueur
    
    def getlargeur(self):
        return self.__largeur

class Parallélépipède(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)
        self.hauteur = hauteur

    def volume(self):
        # multiplier longueur, largeur, hauteur
        self.longueur = self.getlongueur()
        self.largeur = self.getlargeur()
        somme = self.longueur * self.largeur * self.hauteur
        return somme

rect = Rectangle(5, 10)

parallélépipède1 = Parallélépipède(5, 10, 15)

print('Périmètre:', rect.périmètre())

print('Surface:', rect.surface())

print('Volume:', parallélépipède1.volume())