import unittest
from gestion_taches import GestionTaches
from projet import Projet


class TestProjetIntegration(unittest.TestCase):

    def test_ajouter_tache_au_projet(self):
        gestion_taches = GestionTaches()
        projet = Projet("Nom du Projet", gestion_taches)

        projet.ajouter_tache_au_projet("Tâche 5", "Description de la tâche 5")
        self.assertIn("Tâche 5", gestion_taches.taches)


if __name__ == '__main__':
    unittest.main()