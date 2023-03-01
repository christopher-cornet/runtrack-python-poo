class Tache:
    def __init__(self, titre, description, statut='A faire'):
        self.titre = titre
        self.description = description
        self.statut = statut

class ListeDeTaches:
    def __init__(self):
        self.liste_taches = []

    # ajouter une tache
    def ajouterTache(self, titre):
        self.liste_taches.append(titre)
    
    # supprimer une tache
    def supprimerTache(self, titre):
        self.liste_taches.remove(titre)

    # signaler que la tache est faite.
    def marquerCommeFinie(self):
        # self.liste_taches.append('Finie')
        pass
    
    # retourner une liste de toutes les taches.
    def afficherListe(self):
        for tache in self.liste_taches:
            print(f'{tache.titre} - {tache.description} - {tache.statut}')

    # filtrer les taches par rapport à un statut et retourne
    # cette liste.
    def filterListe(self):
        pass

tache1 = Tache('coder', 'apprendre la POO')
tache2 = Tache('réparer voiture', 'changer la batterie')

taches = ListeDeTaches()

taches.ajouterTache(tache1)
taches.ajouterTache(tache2)

print("Liste des taches:")
taches.afficherListe()