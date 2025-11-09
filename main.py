""" main.py """
from scrapping.main import ecrire_data
from scrapping.scrap_data import scrap_data
from scrapping.scrap_liste_recettes import get_all_recipe_slugs
from scrapping.const import SITE, AVIS, EXTENSION

if __name__ == "__main__":
    slugs = get_all_recipe_slugs()
    urls = [f"{SITE}{AVIS}{slug}{EXTENSION}" for slug in slugs]
    comments = scrap_data(urls)
    ecrire_data(comments)
    print(f"Total commentaires récupérés : {len(comments)}")
