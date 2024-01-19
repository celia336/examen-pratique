class Projet:
    def __init__(self, nom, gestion_taches):
        self.nom = nom
        self.gestion_taches = gestion_taches
        self.taches = []

    def ajouter_tache_au_projet(self, titre, description):
        self.gestion_taches.ajouter_tache(titre, description)
        self.taches.append(titre)