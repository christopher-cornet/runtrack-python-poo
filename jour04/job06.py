class Vehicule:
    def __init__(self, marque, modèle, année, prix):
        self.modèle = modèle
        self.marque = marque
        self.année = année
        self.prix = prix

    def informationsVehicule(self):
        print(self.marque, self.année, self.prix)

    def demarrer(self):
        print('Attention, je roule')

class Voiture(Vehicule):
    def __init__(self, marque, modèle, année, prix, portes):
        super().__init__(marque, modèle, année, prix)
        self.modèle = modèle
        self.portes = portes

    def informationsVehicule(self):
        print('Marque =', self.marque)
        print('Model =', self.modèle)
        print('Année =', self.année)
        print('Prix =', self.prix)
        print('Nombre de portes =', self.portes)

    def demarrer(self):
        print('Attention, je roule avec une voiture', self.marque, 'et elle coute', self.prix, '€')

class Moto(Vehicule):
    def __init__(self, marque, modèle, année, prix, roue):
        super().__init__(marque, modèle, année, prix)
        self.modèle = modèle
        self.roue = roue

    def informationsVehicule(self):
        print('Marque =', self.marque)
        print('Model =', self.modèle)
        print('Année =', self.année)
        print('Prix =', self.prix)
        print('Nombre de roues =', self.roue)

    def demarrer(self):
        print('Attention, je roule avec une moto', self.marque, 'et elle coute', self.prix, '€')

# Instance voiture
vehicule1 = Voiture('Lamborghini', 'Huracan STO', 2017, 299294, 2)

# Instance moto
vehicule2 = Moto('Kawasaki', 'Ninja H2', 2019, 50000, 2)

# Print les infos voiture
vehicule1.informationsVehicule()

# Print les infos moto
vehicule2.informationsVehicule()

# Démarrer la voiture
vehicule1.demarrer()

# Démarrer la moto
vehicule2.demarrer()