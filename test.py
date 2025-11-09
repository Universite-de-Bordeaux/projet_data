from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

# Exemple de corpus
corpus = [
    "Le chat dort sur le canapé",
    "Le chien joue dans le jardin",
    "Le chat et le chien mangent"
]

vectorizer = CountVectorizer()
X_counts = vectorizer.fit_transform(corpus)

print(vectorizer.get_feature_names_out())  # mots extraits
print(X_counts.toarray(), "\n")            # matrice de comptage

tfidf = TfidfVectorizer()
X_tfidf = tfidf.fit_transform(corpus)

print(tfidf.get_feature_names_out())  # mots extraits
print(X_tfidf.toarray())              # matrice pondérée
