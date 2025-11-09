# Analyse de commentaire de marmiton.org

## Objectif du projet
Sur marmiton.org, beaucoup de recettes sont disponibles. Les utilisateurs peuvent partager directement sur la plateforme depuis la section commentaire de chaque recette. On souhaite traiter ses commentaires afin d'en tirer le plus d'informations possibles.

## Structure du projet
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
En utilisant les sitemaps XML de Marmiton, on a pu récupérer toutes les recettes disponible depuis les adresses de la forme https://marmiton.org/recettes/recette_[slug].aspx avec slug un indentifiant unique à chaque page.  
On a aussi remarqué la correspondance avec une autre adresse qui correspond à la liste des commentaires d'une page donnée : https://marmiton.org/recettes/recette-avis_[slug].aspx.  
Il suffit ensuite de récupérer chaque commentaire (marqué par la balise p de classe recipe-reviews-list__review__text).  

### Enregistrement des données
On a décidé d'enregistrer les données dans un json sous la forme suivante :  
{
    "com_id": [id du commentaire],  
    "com_text": [texte du commentaire],  
    "com_recipe_id": [page de recette],  
    "com_author": [pseudo],  
    "com_date": [date]  
}

### Calcul d'occurences tfidf

### Projection PCA interactive

## Membres du projet
BRUNEAU Vincent
MARI Micky