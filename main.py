""" main.py """
from scrapping.main import ecrire_data
from scrapping.scrap_data import scrap_data
from scrapping.scrap_liste_recettes import get_all_recipe_slugs

if __name__ == "__main__":
    slugs = get_all_recipe_slugs()
    comments = scrap_data(slugs)
    ecrire_data(comments)
    print(f"Total commentaires récupérés : {len(comments)}")
