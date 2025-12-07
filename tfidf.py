""" tfidf.py """

import json
from sklearn.feature_extraction.text import TfidfVectorizer

def calculer_tfidf(corpus: list[str], stop_words:str | list[str] = None, min_df:int = 1, max_df:float = 1.0):
    """Calcule la matrice TF-IDF pour un corpus donné"""
    tfidf = TfidfVectorizer(stop_words=stop_words, min_df=min_df, max_df=max_df)
    X_tfidf = tfidf.fit_transform(corpus) # pylint:disable=invalid-name
    return tfidf, X_tfidf

def sauvegarder_tfidf(X_tfidf, filename = "tfidf.json"):
    """ Sauvegarde la matrice TF-IDF au format JSON """
    json_data = [{
                    "longueur": X_tfidf.shape[0],
                    "largeur": X_tfidf.shape[1],
                }]

    for i in range(X_tfidf.shape[0]):
        for j in range(X_tfidf.shape[1]):
            if X_tfidf.toarray()[i][j] != 0:
                json_data.append({
                    "x": i,
                    "y": j,
                    "valeur": X_tfidf.toarray()[i][j],
                })

    with open(filename, "w", encoding="utf-16") as f:
        json.dump(json_data, f, indent=4, ensure_ascii=False)

def load_matrice(filename = "tfidf.json"):
    """ Charge la matrice TF-IDF depuis un fichier JSON """
    with open(filename, "r", encoding="utf-16") as f:
        json_data = json.load(f)

    size = json_data.pop(0)
    matrix = []
    for _ in range(size["longueur"]):
        l = [0] * size["largeur"]
        matrix.append(l)
    for data in json_data:
        matrix[data["x"]][data["y"]] = data["valeur"]
    return matrix
