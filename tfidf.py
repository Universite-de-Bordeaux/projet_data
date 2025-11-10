""" tfidf.py """

from sklearn.feature_extraction.text import TfidfVectorizer
import json

def calculer_tfidf(corpus: list[str]):
    """Calcule la matrice TF-IDF pour un corpus donné"""
    tfidf = TfidfVectorizer()
    X_tfidf = tfidf.fit_transform(corpus) # pylint:disable=invalid-name
    return tfidf, X_tfidf

def sauvegarder(X_tfidf, filename = "tfidf.json"):
    json_data = []

    for i in range(len(X_tfidf.toarray())):
        for j in range(len(X_tfidf.toarray()[i])):
            if X_tfidf.toarray()[i][j] != 0:
                json_data.append({
                    "x": i,
                    "y": j,
                    "valeur": X_tfidf.toarray()[i][j],
                })

    with open(filename, "w", encoding="utf-16") as f:
        json.dump(json_data, f, indent=4, ensure_ascii=False)

