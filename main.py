""" main.py """
import time
from sklearn.cluster import KMeans
from stop_words import get_stop_words
from scrapping.main import ecrire_data, ecrire_data_safe
from scrapping.scrap_data import scrap_data
from scrapping.scrap_liste_recettes import get_all_recipe_slugs
from tfidf import calculer_tfidf, sauvegarder_tfidf
from sentiments import a_sentiments, mots_caracteristiques_kmeans
from cartographie import projec_pca_interactive
from reader_data import read_data, extracte_data_unique

mot_local = ["recette", "très"]

def gen_data():
    """ Pour générer le fichier datas.json """
    start = time.time()
    slugs = get_all_recipe_slugs()
    datas = scrap_data(slugs, nb_slug=10, nb_workers=1)
    ecrire_data(datas)
    end = time.time()
    print(f"Temps écoulé pour le scrapping : {end - start} secondes")

if __name__ == "__main__":
    # gen_data()
    # ecrire_data_safe("datas/datas_all_slugs.json", nb_workers=15, max_slugs=100000)
    datas = read_data("datas/datas_27_000_slugs_presque_corrige.json")
    # extracte_data_unique()
    print(f"Total commentaires récupérés : {len(datas)}")

    # # Calcul du TF-IDF sur les commentaires agrégés par recette
    # groupes = {}
    # for com_id, (text, recipe_id, author, date) in datas.items():
    #     groupes.setdefault(recipe_id, []).append(text)
    # _, X_tfidf = calculer_tfidf(groupes)
    # sauvegarder_tfidf(X_tfidf, "comments_by_recipe.json")
    # comments_by_recipe = [";".join(texts) for recipe_id, texts in groupes.items()]

    # # Création de la projection PCA interactive correspondante
    # projec_pca_interactive(comments_by_recipe, X_tfidf)

    # Calcul du TF-IDF sur les commentaires
    coms = [text for text, _, _, _ in datas.values()]
    vectorizer, X_tfidf = calculer_tfidf(coms, stop_words=get_stop_words('french') + mot_local , min_df=5, max_df=0.9)
    N_CLUSTERS = 3
    clusters = a_sentiments(X_tfidf, N_CLUSTERS, random_state=42)

    keywords = mots_caracteristiques_kmeans(
        kmeans=KMeans(n_clusters=N_CLUSTERS).fit(X_tfidf),
        vectorizer=vectorizer,
        top_n=10
    )

    print("Mots caractéristiques par cluster :")
    for cluster_id, keywords_list in keywords.items():
        print(f"Cluster {cluster_id} : {', '.join(keywords_list)}")

    projec_pca_interactive(coms, X_tfidf, "proj_pca.html")
    projec_pca_interactive(coms, X_tfidf, "proj_pca_clusters.html", clusters)
