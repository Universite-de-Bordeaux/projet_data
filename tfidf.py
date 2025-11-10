""" tfidf.py """

from sklearn.feature_extraction.text import TfidfVectorizer
import json

def calculer_tfidf(corpus: list[str]):
    """Calcule la matrice TF-IDF pour un corpus donné"""
    tfidf = TfidfVectorizer()
    X_tfidf = tfidf.fit_transform(corpus) # pylint:disable=invalid-name
    return tfidf, X_tfidf

def sauvegarder(X_tfidf, filename = "tfidf.json"):
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
    with open(filename, "r", encoding="utf-16") as f:
        json_data = json.load(f)

    size = json_data.pop(0)
    matrix = []
    for i in range(size["longueur"]):
        l = [0] * size["largeur"]
        matrix.append(l)
    for data in json_data:
        matrix[data["x"]][data["y"]] = data["valeur"]
    return matrix

