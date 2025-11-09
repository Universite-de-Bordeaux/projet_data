""" main.py """
# pylint: disable=line-too-long

import json
from .const import SITE, AVIS, EXTENSION, MAX_SLUG
from .scrap_data import scrap_data
from .scrap_liste_recettes import get_all_recipe_slugs

def main()->list[str]:
    """Fonction principale du module."""
    print("Démarrage du scrapping des commentaires")
    liste_recettes = get_all_recipe_slugs()

    # URLs à scrapper
    slugs = [slug for slug in liste_recettes[:min(MAX_SLUG, len(liste_recettes))]]
    print([f"{SITE}{AVIS}{slug}{EXTENSION}" for slug in slugs])
    dico = scrap_data(slugs)
    print(dico)
    return dico

def ecrire_data(data, filename="comments.json") -> None:
    """Écrit les commentaires dans un fichier JSON valide."""
    # data doit être un dictionnaire sous la forme :
    # {com_id: [com_text, com_recipe_id, com_author, com_date], ...}

    json_data = []

    for key, value in data.items():
        json_data.append({
            "com_id": key,
            "com_text": value[0],
            "com_recipe_id": value[1],
            "com_author": value[2],
            "com_date": value[3]
        })

    with open(filename, "w", encoding="utf-16") as f:
        json.dump(json_data, f, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    datas = main()
    ecrire_data(datas)
