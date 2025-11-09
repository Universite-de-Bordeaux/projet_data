""" main.py """
from scrapping.main import ecrire_data
from scrapping.scrap_data import scrap_data
from scrapping.scrap_liste_recettes import get_all_recipe_slugs
from tfidf import calculer_tfidf
from cartographie import projec_pca_interactive
from reader_data import read_data

def gen_data():
    """ Pour générer le fichier datas.json """
    slugs = get_all_recipe_slugs()
    datas = scrap_data(slugs, nb_slug=100, nb_workers=10) 
    ecrire_data(datas)

if __name__ == "__main__":
    # gen_data()
    datas = read_data()
    print(f"Total commentaires récupérés : {len(datas)}")

    # Calcul du TF-IDF
    groupes = {}
    for com_id, (text, recipe_id, author, date) in datas.items():
        groupes.setdefault(recipe_id, []).append(text)
    _, X_tfidf = calculer_tfidf(groupes)

    # Création de la projection PCA interactive
    projec_pca_interactive(datas, X_tfidf)
