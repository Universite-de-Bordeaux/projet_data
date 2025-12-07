import json

def lire_fichier(chemin: str) -> str:
    """Lit entièrement un fichier et renvoie son contenu."""
    with open(chemin, "r", encoding="utf-16") as f:
        return f.read()


def fusionner_lignes(texte: str) -> str:
    """Fusionne les lignes qui ne commencent pas par [, { ou " avec la ligne précédente."""
    lignes = texte.splitlines()
    resultat = []

    for ligne in lignes:
        stripped = ligne.lstrip()

        if stripped.startswith(('[', '"', '{')):
            resultat.append(ligne)
        else:
            if resultat:
                resultat[-1] = resultat[-1] + stripped
            else:
                resultat.append(stripped)

    return "\n".join(resultat)


def ecrire_fichier(chemin: str, contenu: str):
    """Écrit du texte dans un fichier."""
    with open(chemin, "w", encoding="utf-16") as f:
        f.write(contenu)

def ajout_saut_ligne_avant_com(texte: str) -> str:
    """
    Ajoute un saut de ligne après chaque virgule si elle est immédiatement suivie de "com_".
    """
    resultat = []
    i = 0
    while i < len(texte):
        # Si on trouve une virgule
        if texte[i] == ',':
            # Vérifier si les caractères suivants forment "com_"
            if texte[i+1:i+5] == '"com_':
                resultat.append(',\n')
                i += 1
                continue
        resultat.append(texte[i])
        i += 1

    return ''.join(resultat)



def fusionner_lignes(texte: str) -> str:
    lignes = texte.splitlines()
    resultat = []

    for ligne in lignes:
        stripped = ligne.lstrip()

        # Si la ligne commence par un caractère ouvrant → nouvelle ligne normale
        if stripped.startswith(('[', '"', '{', '}', ']')):
            resultat.append(ligne)
        else:
            # Sinon on fusionne avec la ligne précédente
            if resultat:
                resultat[-1] = resultat[-1] + stripped
            else:
                resultat.append(stripped)

    return "\n".join(resultat)

def saut_de_ligne_qui_demarre_par_guillemet(texte: str) -> str:
    """
    Supprime les sauts de ligne après les lignes qui semblent incomplètes
    (ne commencent pas par { [ ] }, et ne se terminent pas par ,).
    La ligne suivante est concaténée à la fin de la ligne courante.
    """
    lignes = texte.splitlines()
    resultat = []
    skip_next = False

    for i, ligne in enumerate(lignes):
        if skip_next:
            skip_next = False
            continue

        stripped = ligne.strip()
        if not stripped:
            resultat.append(ligne)
            continue

        # Si ligne incomplète
        if stripped[0] not in "{[}]" and not stripped.endswith(",") and i + 1 < len(lignes):
            # Concaténer la ligne suivante
            nouvelle_ligne = ligne.rstrip() + " " + lignes[i + 1].lstrip()
            resultat.append(nouvelle_ligne)
            skip_next = True
        else:
            resultat.append(ligne)

    return "\n".join(resultat)


def char_replacement(texte: str) -> str:
    """Nettoie le texte : remplace tabulations et guillemets comme souhaité."""
    quotes_set = {'"', '“', '”'}
    resultat = []

    for ligne in texte.splitlines(keepends=False):
        # 1. Remplacement des tabulations et autres caractères de contrôle par espace
        ligne = ''.join(c if ord(c) >= 32 else ' ' for c in ligne)

        # 2. Remplacement des antislash par slash
        ligne = ligne.replace("\\", "/")

        chars = list(ligne)
        positions = []

        # 3. Repérer positions des guillemets
        for i, c in enumerate(chars):
            if c in quotes_set:
                positions.append(i)

        # 4. Si moins de 5 guillemets, on ne modifie rien
        if len(positions) > 4:
            # Remplacer tous les guillemets entre le 4ᵉ et l'avant-dernier
            for pos in positions[3:-1]:
                chars[pos] = "'"

        resultat.append("".join(chars))

    return "\n".join(resultat)


def detecte_cle_manquante(data, required_keys):
    """
    Vérifie pour chaque commentaire si des clés obligatoires sont manquantes.
    """
    missing = {}

    for comment in data:
        com_id = comment.get("com_id", "<ID manquant>")
        missing_keys = [k for k in required_keys if k not in comment]
        if missing_keys:
            missing[com_id] = missing_keys

    return missing


# Exemple d'utilisation :
texte = lire_fichier("datas/datas_27_000_slugs.json")
texte = fusionner_lignes(texte)
texte = ajout_saut_ligne_avant_com(texte)
texte = saut_de_ligne_qui_demarre_par_guillemet(texte)
texte = char_replacement(texte)
ecrire_fichier("output2.txt", texte)
manquants = detecte_cle_manquante(
    json.loads(texte),
    required_keys=["com_id", "com_text", "com_recipe_id", "com_author", "com_date"]
)
print("Commentaires avec clés manquantes :", manquants)