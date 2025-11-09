from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

NB_CHAPITRE_NO_SPOIL = 3

# Lecture du fichier
def extract_text(FileName="Partie 1 Luc et Mélissa.txt", spoil = NB_CHAPITRE_NO_SPOIL):
    with open(FileName, "r", encoding="utf-8") as f:
        contenu = f.read()
    return tronque_spoil(contenu, spoil)

def tronque_spoil(contenu, nb_chapitre_max):
    retour = ""
    j = 0
    for i in range(nb_chapitre_max):
        j = contenu.find("chapitre", j, len(contenu))
        if j == -1:
            print("aucun spoil détecté")
            return contenu
        retour += contenu[0:j+11]
        contenu = contenu[j:]
    print("barrière anti spoil déployée !")
    return retour

def test():
    stop_words_fr = [
        "le", "la", "les", "de", "des", "du", "un", "une",
        "et", "en", "dans", "au", "aux", "ce", "cet", "cette",
        "il", "elle", "ils", "elles", "nous", "vous", "je", "tu",
        "se", "sa", "son", "ses", "leur", "leurs", "y", "à", "pour",
        "que", "qu", "lui", "qui", "sur", "par", "'", ".", ",", ";", "ton",
        "tes", "ta", "me", "nos", "vos", "notre", "votre", "ces", "on", "\""
    ]

    contenu = [extract_text()]
    # Vectorisation
    vectorizer = CountVectorizer(stop_words = stop_words_fr)
    X = vectorizer.fit_transform(contenu)

    # Récupération du vocabulaire et des fréquences
    mots = vectorizer.get_feature_names_out()
    frequences = X.toarray()[0]

    # Associer mots et fréquences
    mots_freq = list(zip(mots, frequences))

    # Trier par fréquence décroissante
    mots_freq_sorted = sorted(mots_freq, key=lambda x: x[1], reverse=True)

    tfidf = TfidfVectorizer(stop_words = stop_words_fr)
    X_tfidf = tfidf.fit_transform(contenu)

    portion = X_tfidf.toarray()[0]
    mots_portion = list(zip(mots, portion))

    mots_portion_sorted = sorted(mots_portion, key=lambda x: x[1], reverse=True)

    # Afficher les 20 mots les plus fréquents
    sizemot = 17
    sizefreq = 20
    sizeocc = 18
    size1 = 7
    significatif_occ = 0
    significatif_freq = 0
    significati_par_chap = 0
    nb_chapitre = NB_CHAPITRE_NO_SPOIL

    print("indice | mot               | fréquence            | nombre d'occurence | fréquence par chapitre\n")
    for i in range(len(mots_portion_sorted)):
        nb_espace = size1
        nb_espace -= 3
        if i >= 9:
            nb_espace -= 1
        if i >= 99:
            nb_espace -= 1
        if i >= 999:
            nb_espace -= 1
        espace = " " * nb_espace

        mot = mots_portion_sorted[i][0]
        while len(mot) < sizemot:
            mot += " "

        freq = mots_portion_sorted[i][1]
        if freq < significatif_freq:
            print("fréquence trop basse")
            break

        freq = str(freq)
        while len(freq) < sizefreq:
            freq += " "

        occur = mots_freq_sorted[i][1]
        if occur < significatif_occ:
            print("nombre d'occurence trop faible")
            break

        occur_chap = occur / nb_chapitre
        if occur_chap < significati_par_chap:
            print("nombre d'occurence par chapitre trop faible")
            break

        occur = str(occur)
        while len(occur) < sizeocc:
            occur += " "

        print(f"n°{i + 1}{espace}| {mot} | {freq} | {occur} | {occur_chap}")
