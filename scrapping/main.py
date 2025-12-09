""" main.py """
# pylint: disable=line-too-long

import json
from threading import Lock
from concurrent.futures import ThreadPoolExecutor
from .const import MAX_SLUG, MAX_WORKERS
from .scrap_data import scrap_data, scrap_data_from_url
from .scrap_liste_recettes import get_all_recipe_slugs

def main()->list[str]:
    """Fonction principale du module."""
    print("Démarrage du scrapping des commentaires")
    liste_recettes = get_all_recipe_slugs()

    # URLs à scrapper
    slugs = [slug for slug in liste_recettes[:min(MAX_SLUG, len(liste_recettes))]]
    dico = scrap_data(slugs)
    return dico

def ecrire_data(data, filename="datas.json") -> None:
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

def ecrire_data_safe(filename="datas.json", nb_workers=MAX_WORKERS, max_slugs=MAX_SLUG) -> None:
    """
    Écrit les commentaires dans un fichier JSON au fur et à mesure.
    """

    # Récupération des slugs à traiter
    all_slugs = get_all_recipe_slugs()
    slugs = all_slugs[:min(max_slugs, len(all_slugs))]

    # Préparer les paires (indice, slug)
    slug_pairs = list(enumerate(slugs))

    # Pour éviter les conflits d'écriture
    write_lock = Lock()

    # Fonction pour scrapper et écrire directement
    def scrap_and_write(pair):
        idx, slug = pair
        data = scrap_data_from_url(slug)
        with write_lock:
            with open(filename, "a", encoding="utf-16") as f:
                for key, value in data.items():
                    com_text = value[0]
                    com_text = com_text.replace("\t", " ")
                    com_text = com_text.replace("\n", "")
                    com_text = com_text.replace("\\", "/")
                    com_text = com_text.replace('"', "'")
                    f.write("{\n")
                    f.write(f'\t"com_id" : "{key}",\n')
                    f.write(f'\t"com_text" : "{com_text}",\n')
                    f.write(f'\t"com_recipe_id" : "{value[1]}",\n')
                    f.write(f'\t"com_author" : "{value[2]}",\n')
                    f.write(f'\t"com_date" : "{value[3]}"\n')
                    f.write("},\n")
            print(f"Dernier slug traité : {idx} ({slug})")

    # Lancement du scrapping en parallèle
    with ThreadPoolExecutor(max_workers=nb_workers) as executor:
        executor.map(scrap_and_write, slug_pairs)

if __name__ == "__main__":
    datas = main()
    ecrire_data(datas)

