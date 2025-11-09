""" reader_data.py """

import json

def read_data(filename="comments.json") -> dict:
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
