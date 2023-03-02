class Forme:
    def __init__(self):
        pass

    def aire(self):
        return 0
    
class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        super().__init__()
        self.largeur = largeur
        self.hauteur = hauteur

    def aire(self):
        return self.largeur * self.hauteur

aire_rect = Rectangle(5, 10)

print('Aire du rectangle:', aire_rect.aire(), 'cm²')