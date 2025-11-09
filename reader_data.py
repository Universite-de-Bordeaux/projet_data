""" reader_data.py """

import json

def read_data(filename="datas.json") -> dict:
    """Lit les commentaires depuis un fichier JSON et renvoie un dictionnaire."""
    try:
        with open(filename, "r", encoding="utf-16") as f:
            json_data = json.load(f)

        data = {}
        for com in json_data:
            data[com["com_id"]] = [
                com["com_text"],
                com["com_recipe_id"],
                com["com_author"],
                com["com_date"]
            ]
        return data

    except FileNotFoundError:
        print(f"Le fichier {filename} n'existe pas.")
        return {}

def extracte_data_unique(filename="datas.json"):
    """
    Lit les commentaires depuis un fichier JSON et renvoie un dictionnaire.
    """
    try:
        with open(filename, "r", encoding="utf-16") as f:
            json_data = json.load(f)

        c = 0
        set_commentaire = set()
        set_recipe = set()
        set_author = set()
        set_date = set()
        for com in json_data:
            set_commentaire.add(com["com_text"])
            set_recipe.add(com["com_recipe_id"])
            set_author.add(com["com_author"])
            set_date.add(com["com_date"])
            c += 1
        #print(set_commentaire)
        print(set_recipe)
        print(set_author)
        print(set_date)
        print(f"{c} commentaires extrait depuis {filename}.")
        print(f"{len(set_commentaire)} commentaires unique.")
        print(f"{len(set_recipe)} recette unique.")
        print(f"{len(set_author)} auteur unique.")
        print(f"{len(set_date)} dates unique.")
        return c, len(set_commentaire), len(set_recipe), len(set_author), len(set_date)

    except FileNotFoundError:
        print(f"Le fichier {filename} n'existe pas.")
        return {}

extracte_data_unique()