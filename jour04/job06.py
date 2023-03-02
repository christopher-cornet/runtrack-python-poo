class Vehicule:
    def __init__(self, marque, année, prix):
        self.marque = marque
        self.année = année
        self.prix = prix

    def informationsVehicule(self):
        print(self.marque, self.année, self.prix)

class Voiture(Vehicule):
    def __init__(self, marque, modèle, année, prix, portes):
        super().__init__(marque, année, prix)
        self.modèle = modèle
        self.portes = portes

    def informationsVehicule(self):
        print('Marque =', self.marque)
        print('Model =', self.modèle)
        print('Année =', self.année)
        print('Prix =', self.prix)
        print('Nombre de portes =', self.portes)

vehicule1 = Vehicule('Rolls-Royce Phantom VIII', 2017, 500000)

vehicule2 = Voiture('Lamborghini', 'Huracan STO', 2017, 299294, 2)

vehicule2.informationsVehicule()