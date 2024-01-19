def calculer_duree_totale(taches):
    return sum(tache.get("duree", 0) for tache in taches)