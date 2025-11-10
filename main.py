""" main.py """
from scrapping.main import ecrire_data
from scrapping.scrap_data import scrap_data
from scrapping.scrap_liste_recettes import get_all_recipe_slugs
from tfidf import calculer_tfidf, sauvegarder
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

    # Calcul du TF-IDF sur les commentaires agrégés par recette
    groupes = {}
    for com_id, (text, recipe_id, author, date) in datas.items():
        groupes.setdefault(recipe_id, []).append(text)
    _, X_tfidf = calculer_tfidf(groupes)
    sauvegarder(X_tfidf, "test.json")
    comments_by_recipe = [";".join(texts) for recipe_id, texts in groupes.items()]
    
    # Création de la projection PCA interactive correspondante
    projec_pca_interactive(comments_by_recipe, X_tfidf)

    # Calcul du TF-IDF sur les commentaires
    type(datas)
    coms = [text for text, _, _, _ in datas.values()]
    _, X_tfidf = calculer_tfidf(coms)
    sauvegarder(X_tfidf, "test.json")
    projec_pca_interactive(coms, X_tfidf, "projection_pca_interactive_coms.html")

    # Création de la projection PCA interactive correspondante
    projec_pca_interactive(coms, X_tfidf)