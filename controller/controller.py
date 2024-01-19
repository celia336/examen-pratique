class Controller:
    def __init__(self, gestion_taches):
        self.gestion_taches = gestion_taches

    def afficher_liste_taches(self):
        return list(self.gestion_taches.taches.keys())

    def afficher_tache_par_nom(self, titre):
        tache = self.gestion_taches.taches.get(titre, {})
        return f"Titre: {titre}, Description: {tache.get('description', '')}, Complet: {tache.get('complet', False)}"