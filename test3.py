from random import randint

import spacy
from spacy.language import Language
from spacy.pipeline import Sentencizer
from test2 import extract_text

# Charger le modèle français
# fr_core_news_sm <= python -m spacy download fr_core_news_sm
# fr_core_news_md <= python -m spacy download fr_core_news_md
# fr_core_news_lg <= python -m spacy download fr_core_news_lg


def factory_name(ponctuation):
    """
    Permet de changer le sentencizer (identificiant les séparateurs de phrase) sans tout modifier à la main
    N'est pas destiné à être utilisé seul, il s'agit d'un auxiliaire d'init_nlp
    :param ponctuation: les charactères marquant la fin d'une phrase
    :type ponctuation: Iterable[str] | list[str] | tuple[str]
    """
    @Language.factory("custom_sentencizer")
    def new_custom_sentencizer(nlp, name):
        return Sentencizer(punct_chars=ponctuation)
    custom_sentencizer = new_custom_sentencizer

def init_nlp(langage = "fr_core_news_md", ponctuation = (".", "!", "?", "...", "«", "»", "\n")):
    """
    Crée un nouveau parseur de langage
    :param langage: le langage du parseur (en français, il s'agit de fr_core_news_ + (sm, md ou lg)
    :param ponctuation: les charactères marquant la fin d'une phrase
    :return: le parseur de langage
    :type langage: str
    :type ponctuation: Iterable[str] | list[str] | tuple[str]
    :rtype: spacy.lang.fr.French
    """
    nlp = spacy.load(langage)
    factory_name(ponctuation)
    nlp.add_pipe("custom_sentencizer", first=True)
    return nlp

def make_doc(nlp, caractere_invalide = ("«", "»", "\"", "(", ")"), caractere_a_remplacer = {"\n" : " "},
             Filename : str = "Partie 1 Luc et Mélissa.txt", extension = ".txt"):
    """
    Créer un document spacy
    :param nlp: le parseur de langage
    :param caractere_invalide: les caractères à suprimmer du document
    :param caractere_a_remplacer : les caractères à remplacer du document
    :param Filename: le nom du fichier où se trouvent les informations
    :param extension: le type d'extension du fichier
    :return: un document spacy
    :type nlp: spacy.lang.fr.French
    :type caractere_invalide: Iterable[str] | list[str] | tuple[str]
    :type caractere_a_remplacer: dict[str, str] | None
    :type Filename: str
    :type extension: str
    :rtype: spacy.tokens.doc.Doc
    """
    if extension == ".txt":
        brut = extract_text(Filename)
    else:
        brut = "Pas encore codé mdr"
    text_filtre = ""
    for l in brut:
        if l in caractere_a_remplacer:
            text_filtre += caractere_a_remplacer[l]
        elif l not in caractere_invalide:
            text_filtre += l
    return nlp(text_filtre)

def test_tokens(doc):
    """
    Une fonction test qui affiche différents tokens d'un document
    :param doc: un document spacy
    :type doc: spacy.tokens.doc.Doc
    :rtype: None
    """
    for token in doc:
        print(token.text, token.lemma_, token.pos_, token.dep_)

def test_similarite(nlp, doc):
    """
    Une fonction test qui prend deux phrases aléatoirement, les affiches et affiche leur similarité cosinus
    :param nlp: le parseur de langage
    :param doc: le document spacy
    :type nlp: nlp: spacy.lang.fr.French
    :type doc: spacy.tokens.doc.Doc
    :rtype: None
    """
    i = randint(0, 250)
    j = randint(0, 250)
    text_i = ""
    text_j = ""
    c = 0
    #secmenter par phrase
    for text in doc.sents:
        c += 1
        if c == i:
            text_i = str(text)
        if c == j:
            text_j = str(text)

    print(f"text 1 :\n{text_i}\n\n\ntext 2 :\n{text_j}")
    doc2 = nlp(text_i)
    doc3 = nlp(text_j)
    print(f"similarité cosinus : {doc3.similarity(doc2)}")

def test_nommees(doc, label : str | list[str] | None = None):
    """
    Renvoie tous les mots classés dans une catégorie particulière nom propre, date, évènements, etc.)
    :param doc: le document spacy
    :param label: la ou les catégories particulières voulues
    :type doc: spacy.lang.fr.French
    :type label: str | list[str] | None
    :rtype: None
    """
    retour = set()
    if label is None:
        for ent in doc.ents:
            retour.add((ent.text, ent.label_))
        return retour

    return {ent.text for ent in doc.ents if ent.label_ in label}

def similarite(doc, doc2):
    print(doc.similarity(doc2))
    return doc.similarity(doc)

langage_parser = init_nlp()
doc1 = make_doc(langage_parser)
test_similarite(langage_parser, doc1)
print(f"\nPersonnages : {test_nommees(doc1, 'PER')}")