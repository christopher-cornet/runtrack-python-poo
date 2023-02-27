class Personnage:
    def __init__(self, x, y):
        # Init x et y
        self.x, self.y = x, y
        # Plateau de jeu
        self.tableau = [[1,2,3],[4,5,6],[7,8,9]]
        self.pos = self.tableau[self.x][self.y]

    def haut(self):
        self.y -= 1
        self.pos = self.tableau[self.x][self.y]

    def bas(self):
        self.y += 1
        self.pos = self.tableau[self.x][self.y]

    def gauche(self):
        self.x -= 1
        self.pos = self.tableau[self.x][self.y]

    def droite(self):
        self.x += 1
        self.pos = self.tableau[self.x][self.y]

    def position(self):
        emplacement = (self.x, self.y)
        print('Position du personnage:', emplacement)
        
personnage1 = Personnage(0, 0)

personnage1.droite()
personnage1.droite()
personnage1.position()

personnage1.bas()
personnage1.bas()
personnage1.position()

personnage1.gauche()
personnage1.gauche()
personnage1.position()

personnage1.haut()
personnage1.haut()
personnage1.position()