class Point:
    def __init__(self, x, y):
        # Attributs x et y
        self.x = x
        self.y = y

    # Affiche les points
    def afficherLesPoints(self):
        print('Afficher les points:')
        print('x =', self.x)
        print('y =', self.y)
    
    # Affiche X
    def afficherX(self):
        print('Afficher X: x =', self.x)

    # Affiche Y
    def afficherY(self):
        print('Afficher Y: y =', self.y)

    # Modifier X
    def changerX(self, x):
        self.x = x 
        print('Changer X: x =', x)

    # Modifier Y
    def changerY(self, y):
        self.y = y
        print('Changer Y: y =', y)

# X = 25, Y = 75
point1 = Point(25, 75)

# Appel de la méthode, affiche les points X et Y
point1.afficherLesPoints()

# Affiche les points séparément
point1.afficherX()
point1.afficherY()

# Modifie X et Y
point1.changerX(88)
point1.changerY(99)

# Affiche les points après modification
point1.afficherLesPoints()