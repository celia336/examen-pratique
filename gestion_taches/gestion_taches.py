class GestionTaches:
    def __init__(self):
        self.taches = {}

    def ajouter_tache(self, titre, description):
        self.taches[titre] = {"description": description, "complet": False}

    def completer_tache(self, titre):
        if titre in self.taches:
            self.taches[titre]["complet"] = True

    def verifier_tache(self, titre):
        if titre in self.taches:
            return self.taches[titre]["complet"]
        return False