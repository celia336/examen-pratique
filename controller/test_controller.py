import unittest
from gestion_taches import GestionTaches
from controller import Controller

class TestController(unittest.TestCase):

    def test_afficher_liste_taches(self):
        gestion_taches = GestionTaches()
        controller = Controller(gestion_taches)

        gestion_taches.ajouter_tache("Tâche 6", "Description de la tâche 6")
        gestion_taches.ajouter_tache("Tâche 7", "Description de la tâche 7")

        result = controller.afficher_liste_taches()
        self.assertIn("Tâche 6", result)
        self.assertIn("Tâche 7", result)

    def test_afficher_tache_par_nom(self):
        gestion_taches = GestionTaches()
        controller = Controller(gestion_taches)

        gestion_taches.ajouter_tache("Tâche 8", "Description de la tâche 8")
        result = controller.afficher_tache_par_nom("Tâche 8")

        self.assertIn("Tâche 8", result)
        self.assertIn("Description de la tâche 8", result)

if __name__ == '__main__':
    unittest.main()