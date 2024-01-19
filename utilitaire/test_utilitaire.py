import unittest
from utilitaire import calculer_duree_totale

class TestUtilitaire(unittest.TestCase):

    def test_calculer_duree_totale_liste_vide(self):
        result = calculer_duree_totale([])
        self.assertEqual(result, 0)

    # ... Ajoutez d'autres tests pour la fonction utilitaire ...

if __name__ == '__main__':
    unittest.main()