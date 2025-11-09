""" tfidf.py """
from sklearn.feature_extraction.text import TfidfVectorizer

def calculer_tfidf(corpus: list[str]) -> TfidfVectorizer:
    """ Calcule la matrice TF-IDF pour un corpus donné """
    tfidf = TfidfVectorizer()
    X_tfidf = tfidf.fit_transform(corpus) # pylint: disable=invalid-name
    return tfidf, X_tfidf
