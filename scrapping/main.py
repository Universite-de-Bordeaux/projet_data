""" main.py """
# pylint: disable=line-too-long

from .const import SITE, AVIS, EXTENSION, MAX_SLUG
from .scrap_com import scrap_comments
from .scrap_liste_recettes import get_all_recipe_slugs

def main()->list[str]:
    """Fonction principale du module."""
    print("Démarrage du scrapping des commentaires")
    liste_recettes = get_all_recipe_slugs()

    # URLs à scrapper
    urls = [f"{SITE}{AVIS}{slug}{EXTENSION}" for slug in liste_recettes[:min(MAX_SLUG, len(liste_recettes))]]

    return scrap_comments(urls)

def ecrire_comments_dans_fichier(coms, filename="comments.txt")->None:
    """ Écrit les commentaires dans un fichier texte. """
    with open(filename, "w", encoding="utf-8") as f:
        for comment in coms:
            f.write(comment + "\n")

if __name__ == "__main__":
    comments = main()
    ecrire_comments_dans_fichier(comments)
