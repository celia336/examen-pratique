import unittest
from gestion_taches import GestionTaches

class TestGestionTaches(unittest.TestCase):

    def setUp(self):
        self.gestion_taches = GestionTaches()

    def test_ajouter_tache(self):
        self.gestion_taches.ajouter_tache("Tâche 1", "Description de la tâche 1")
        self.assertIn("Tâche 1", self.gestion_taches.taches)

    # ... Ajoutez d'autres tests unitaires ...

if __name__ == '__main__':
    unittest.main()