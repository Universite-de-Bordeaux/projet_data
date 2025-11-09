# Analyse de commentaire de marmiton.org

Il existe, sur 
[marmiton.org](https://marmiton.org/recettes/recette_[slug].aspx) un grand nombre de recettes disponible.
Ces recettes sont accessibles librement à tous utilisateurs, qui est tout aussi libre
de laisser un commentaire sous celle-ci. Nous souhaitons travailler sur ces derniers, afin de les analyser
et d'en extraire des informations utiles.


## Objectif du projet
Sur marmiton.org, beaucoup de recettes sont disponibles. Les utilisateurs peuvent partager directement sur la plateforme depuis la section commentaire de chaque recette. On souhaite traiter ses commentaires afin d'en tirer le plus d'informations possibles.
- Extraire les commentaires de recettes Marmiton et les stocker de manière traçable.
- Préparer des jeux de données nettoyés pour NLP (TF‑IDF, embeddings, clustering, classification de sentiment).
- Extraire et analyser des informations utiles de ces données 


## Structure du projet
.  
├── cartographie.py  
├── main.py  
├── README.md  
├── scrapping  
│   ├── const.py  
│   ├── __init__.py  
│   ├── main.py  
│   ├── scrap_com.py  
│   └── scrap_liste_recettes.py  
└── venv.sh  

## Méthode

### Récolte des données
En utilisant les sitemaps XML de Marmiton, nous avons pu récupérer les recettes disponibles depuis les adresses de la forme https://marmiton.org/recettes/recette_[slug].aspx avec slug un indentifiant unique à chaque page.  
Nous avons aussi remarqué la correspondance avec une autre adresse : la liste de ses commentaires : https://marmiton.org/recettes/recette-avis_[slug].aspx.  
Il suffit alors de récupérer chaque commentaire (marqué par la balise p de classe recipe-reviews-list__review__text).  

### Enregistrement des données
Nous avons décidé d'enregistrer les données sous le format json de la manière suivante :  

{
    "com_id": `clé primaire`,  
    "com_text": `texte du commentaire`,  
    "com_recipe_id": `page de la recette`,  
    "com_author": `pseudo de l'auteur`,  
    "com_date": `date du commentaire`  
}

### Calcul d'occurences tf-idf


### Projection PCA interactive

## Membres du projet
BRUNEAU Vincent  
MARI Micky