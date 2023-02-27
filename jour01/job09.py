class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA

    # retourne le prix produit avec la TVA.
    def CalculerPrixTTC(self):
        prix_ttc = self.prixHT / 100 * 5.5
        return prix_ttc

    # la méthode “afficher” qui liste l’ensemble des informations du produit.
    def afficher(self):
        return self.nom, self.prixHT, self.TVA

    # Ajouter des méthodes permettant de modifier le nom du produit et son prix.
    def modifNomPrix(self, nom, prixHT):
        self.nom = nom
        self.prixHT = prixHT
        return nom, prixHT

# Créer plusieurs produits et calculer leurs TVA. Nom/prixHT/TVA
produit1 = Produit('Burger', 10, 5)
produit1.CalculerPrixTTC()

produit2 = Produit('Ordinateur', 1500, 10)
produit2.CalculerPrixTTC()

# TVA
print(produit1.CalculerPrixTTC())
print(produit2.CalculerPrixTTC())

# Infos produits
print(produit1.afficher())
print(produit2.afficher())

# Modif nom/prix
produit1.modifNomPrix('GTA 6', 80)
produit2.modifNomPrix('Hogwarts Legacy', 50)

# Infos produits après modification
print(produit1.afficher())
print(produit2.afficher())