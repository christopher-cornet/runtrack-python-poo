class Tache:
    def __init__(self, titre, description, statut):
        self.titre = titre
        self.description = description
        self.statut = statut

class ListeDeTaches:
    def __init__(self):
        self.taches = []

    # ajouter une tache
    def ajouterTache(self, titre):
        self.taches.append(titre)
        print(self.taches)
    
    # supprimer une tache
    def supprimerTache(self, titre):
        self.taches.remove(titre)
        print(self.taches)

    # signaler que la tache est faite.
    def marquerCommeFinie(self):
        self.taches.append('Finie')
    
    # retourner une liste de toutes les taches.
    def afficherListe(self):
        print(self.taches)

    # filtrer les taches par rapport à un statut et retourne
    # cette liste.
    def filterListe(self):
        pass

tache1 = Tache('travailler', 'coder', 'à faire')

tache2 = ListeDeTaches()
tache2.ajouterTache('coder')
tache2.ajouterTache('travailler')
tache2.ajouterTache('travailler')
tache2.supprimerTache('coder')