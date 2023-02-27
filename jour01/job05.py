class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def afficherLesPoints(self):
        print('Afficher les points:')
        print('x =', self.x)
        print('y =', self.y)
    
    def afficherX(self):
        print('Afficher X: x =', self.x)

    def afficherY(self):
        print('Afficher Y: y =', self.y)

    def changerX(self, x):
        self.x = x 
        print('Changer X: x =', x)

    def changerY(self, y):
        self.y = y
        print('Changer Y: y =', y)

point1 = Point(25, 75)

point1.afficherLesPoints()

point1.afficherX()
point1.afficherY()

point1.changerX(88)
point1.changerY(99)

point1.afficherLesPoints()