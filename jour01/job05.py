class Point:
    def __init__(self, x, y):
        x = x
        y = y

    def afficherLesPoints(self, x, y):
        print('Afficher les points:')
        print('x =', x)
        print('y =', y)
    
    def afficherX(self, x):
        print('Afficher X: x =', x)

    def afficherY(self, y):
        print('Afficher Y: y =', y)

    def changerX(self, x):
        print('Changer X: x =', x)

    def changerY(self, y):
        print('Changer Y: y =', y)

point1 = Point(25, 75)

point1.afficherLesPoints(25, 75)

point1.afficherX(25)
point1.afficherY(75)

point1.changerX(88)
point1.changerY(99)