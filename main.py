""" main.py """
from scrapping.main import ecrire_comments_dans_fichier
from scrapping.scrap_com import scrap_comments
from scrapping.scrap_liste_recettes import get_all_recipe_slugs
from scrapping.const import SITE, AVIS, EXTENSION

if __name__ == "__main__":
    slugs = get_all_recipe_slugs()
    urls = [f"{SITE}{AVIS}{slug}{EXTENSION}" for slug in slugs]
    comments = scrap_comments(urls)
    ecrire_comments_dans_fichier(comments)
    print(f"Total commentaires récupérés : {len(comments)}")
