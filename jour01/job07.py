class Personnage:
    def __init__(self, x, y):
        self.x, self.y = x, y
        print('x =', x)
        print('y =', y)

    def haut(self):
        self.y -= 1
        print('Haut: y =', self.y)

    def bas(self):
        self.y += 1
        print('Bas: y =', self.y)

    def gauche(self):
        self.x -= 1
        print('Gauche: x =', self.x)

    def droite(self):
        self.x += 1
        print('Droite: x =', self.x)

    def position(self):
        tuple_coordonnees = (self.x, self.y)
        print('Position du personnage:', tuple_coordonnees)
        
personnage1 = Personnage(10, 30)

personnage1.haut()
personnage1.bas()
personnage1.gauche()
personnage1.droite()

personnage1.position()