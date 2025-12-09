""" Fichier contenant la/les fonction(s) de kmeans """
from sklearn.cluster import KMeans
import numpy as np

def clustering(tfidf_matrix, n_clusters=3, random_state=42):
    """Effectue le clustering K-Means sur la matrice TF-IDF donnée"""
    # Cette fonction regroupe les documents en n_clusters clusters basés sur leurs caractéristiques TF-IDF.
    # KMeans utilise de l'aléatoire, on fixe une graine par défaut pour la reproductibilité.
    # 42 car c'est la réponse à la grande question de l'univers et le reste
    kmeans = KMeans(n_clusters=n_clusters, random_state=random_state)
    clusters = kmeans.fit_predict(tfidf_matrix)
    return clusters

def mots_caracteristiques_kmeans(kmeans, vectorizer, top_n=10):
    """
    Retourne les mots les plus caractéristiques de chaque cluster.
    """

    # Noms de tous les mots du vocabulaire TF-IDF
    terms = np.array(vectorizer.get_feature_names_out())

    # Liste des centres des clusters
    centers = kmeans.cluster_centers_

    clusters_keywords = {}

    for idx, center in enumerate(centers):
        # indices des top_n valeurs les plus élevées dans le centroïde
        top_indices = center.argsort()[::-1][:top_n]

        # mots correspondant aux indices
        top_terms = terms[top_indices]

        clusters_keywords[idx] = top_terms.tolist()

    return clusters_keywords
