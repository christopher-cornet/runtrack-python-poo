class Forme:
    def __init__(self):
        pass

    def aire(self):
        return 0
    
class Cercle(Forme):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def aire(self):
        return (self.radius * self.radius) * 3.14

class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        super().__init__()
        self.largeur = largeur
        self.hauteur = hauteur

    def aire(self):
        return self.largeur * self.hauteur
    
aire_cercle = Cercle(5)
aire_rect = Rectangle(5, 10)

print('Aire du cercle:', aire_cercle.aire(), 'cm²')
print('Aire du rectangle:', aire_rect.aire(), 'cm²')

print("Avec d'autres valeurs:")

aire_cercle = Cercle(42)
aire_rect = Rectangle(12, 26)

print('Aire du cercle:', aire_cercle.aire(), 'cm²')
print('Aire du rectangle:', aire_rect.aire(), 'cm²')