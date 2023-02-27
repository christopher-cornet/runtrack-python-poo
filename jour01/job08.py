class Cercle:
    def __init__(self, rayon):
        # Définir le rayon
        self.rayon = rayon

    def changerRayon(self, newrayon):
        # Modifier le rayon, rayon = nouveau rayon
        self.rayon = newrayon
        print(self.rayon)

    def circonference(self):
        # Circonference = Diamètre * PI
        self.circonference1 = self.diametre1 * 3.14
        # print('Circonférence =', self.circonference1)

    def aire(self):
        # Rayon au carré
        aire_object = self.rayon * self.rayon
        # Rayon multiplié par le nombre pi
        aire_object_pi = aire_object * 3.14
        # Aire
        self.aire_object_result = aire_object_pi
        # print('Aire =', self.aire_object_result)

    def diametre(self):
        # Diamètre = rayon * 2
        self.diametre1 = self.rayon * 2
        # print('Diamètre =', self.diametre1)

    def afficherInfos(self):
        # Affiche les informations des cercles
        print('Infos:')
        print('Circonférence:', self.circonference1)
        print('Diamètre:', self.diametre1)
        print('Aire:', self.aire_object_result)

# Circonférence, aire et diamètre cercle1
cercle1 = Cercle(4)
print('Cercle 1')
cercle1.diametre()
cercle1.circonference()
cercle1.aire()
cercle1.afficherInfos()

print() # Espacement

# Circonférence, aire et diamètre cercle2
cercle2 = Cercle(7)
print('Cercle 2')
cercle2.diametre()
cercle2.circonference()
cercle2.aire()
cercle2.afficherInfos()

# Changer rayon
print() # Espacement
print('Changer rayon:')
cercle1.changerRayon(15)
cercle2.changerRayon(25)