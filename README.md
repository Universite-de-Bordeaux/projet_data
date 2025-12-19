# Analyse de commentaire de marmiton.org


## Objectif
Il existe, sur [marmiton.org](https://marmiton.org/recettes/recette_[slug].aspx), un grand nombre de recettes.
Ces recettes sont accessibles librement à tout utilisateur, qui est tout aussi libre de laisser un commentaire sous celle-ci. Nous souhaitons travailler sur ces derniers, afin de les analyser
et d'en extraire des informations utiles.
- Extraire les commentaires de recettes Marmiton et les stocker de manière traçable (pouvoir retrouver qui l'a écrit sur quelle page).
- Préparer des jeux de données pour TF‑IDF et kmeans.
- Extraire et analyser des informations utiles de ces données.


## Structure
.  
├── datas  
├── cartographie.py   
├── fixjson.py  
├── kmeans.py  
├── main.py  
├── README.md  
├── Partie 1 Luc et Mélissa.txt  
├── projections  
├── proj_pca_clusters.html  
├── proj_pca.html  
├── reader_data.py  
├── scrapping  
│   ├── __init__.py   
│   ├── const.py  
│   ├── main.py  
│   ├── scrap_data.py    
│   └── scrap_liste_recettes.py  
├── README.md  
├── scrapping  
├── test2.py  
├── test3.py  
├── test.py  
├── tfidf  
├── tfidf.py  
└── venv.sh  

## Méthode

### Récolte des données
En utilisant les sitemaps XML de Marmiton, nous avons pu récupérer les recettes disponibles depuis les adresses de la forme https://marmiton.org/recettes/recette_[slug].aspx avec slug un indentifiant unique à chaque page.  
Nous avons aussi remarqué la correspondance avec une autre adresse : la liste de ses commentaires : https://marmiton.org/recettes/recette-avis_[slug].aspx.  
Il suffit alors de récupérer chaque commentaire (marqué par la balise p de classe recipe-reviews-list__review__text). 
La récolte de données est géré dans la librairie scrapping.

### Enregistrement des données
Nous avons décidé d'enregistrer les données sous le format json de la manière suivante :  

{
    "com_id": `clé primaire`,  
    "com_text": `texte du commentaire`,  
    "com_recipe_id": `page de la recette`,  
    "com_author": `pseudo de l'auteur`,  
    "com_date": `date du commentaire`  
}
Il existe sur le projet deux fonctions pour enregistrer. Une qui attend que le scrapping soit terminé, puis enregistre, l'autre qui enregistre pendant le scrapping. (Les deux dans scrapping.main)

### Lecture des données
Pour lire les données écrites, on utilise
reader_data.py
Ce fichier contient la fonction read_data qui prend en argument un fichier json au format vu précédement et retourne le dictionnaire associé.

### Calcul d'occurences tf-idf
Pour le calcul d'occurences tf-idf on utilise sklearn.
Dans le fichier tfidf.py vous trouverez 3 fonctions, la première afin de calculer tfidf. Elle prend comme paramètre le corpus, des stop_words, min_df qui correspond au nombre minimum d'occurence dans le corpus pour être considéré dans tfidf et max_df qui à l'opoosé de min_df défini un pourcentage d'apparition maximum pour apparaitre dans tdidf.
Les paramètres en question sont intéressants pour une analyse de clusters plus tard. La seconde fonction est sauvegarder_tfidf pour sauvegarder la matrice tfidf en json. Et la dernière load_matrice pour charger la matricec tfidf depuis un json

### Kmeans
kmean.py permet l'utilisation de 2 fonctions  
clustering qui permet de créer des clusters depuis une matrice tfidf.
Cette fonction prend aussi en paramètre, n_clusters qui correspond au nombre de cluster souhaité.

mots_caractéristiques_kmeans permettant de récupérer les mots les plus courants de chaque cluster (pour permettre de les déterminer en quelques mots).

### Cartographie
Pour la cartographie, on utilise les librairies pandas, sklearn.decomposition et plotly.express.

Dans ce fichier est présent la fonction projec_pca_interactive qui permet d'afficher une projection pca, interactive (retourné sous format de page html) qui prend en argument des clusters (par défaut None).

## Fichiers tests
Les fichiers tests sont des fichiers qui permettent de prendre en main certaines parties de sklean ou de spacy. Ils permettaient de se donner une idée du fonctionnement des librairies avant de les incorporer au projet.

### test.py
Ce fichier est un exemple simple de tfidf

### test2.py
Ce fichier permet une analyse un peu plus approfondie, comme récupérer les mots les plus fréquents d'un corpus ou des premiers essaies sur des stop_words

### test3.py
Le dernier fichier test a pour objectif la lemmatisation, il s'agit de d'une étape qui n'a pu être réalisé dans le temps consacré au projet.
En utilisant sapcy, ce fichier permet de voir les limites de la lemmatisation de spacy. Par exemple, la reconnaissance de nom propres est mauvaise.

## Fonctionnement
Pour lancer le projet, il faut utiliser main.py à la source du dépôt.
N'hesitez pas à modifier le main !
Pour générer l'environnement virtuel nécessaire au projet, vous pouvez utiliser venv.sh.
Pour activer l'environnement, il suffit d'utiliser : source venv/bin/activate

main.py contient des parties commentées qui peuvent être décommentées pour un usage direct (comme la génération de carte).
De la même façon, vous pouvez changer l'objet de l'analyse. Nous avons choisis de nous intéresser à l'ensemble des commentaires, mais considérer les commentaires d'un même site de référence peut-être intéressant.

La partie scrapping peut-être lancé indépendamment, il suffit d'utiliser :
python3 -m scrapping.main

## Dossiers
De façon a mieux organiser les fichiers, il existe 3 dossiers.

### datas
Pour les datas collectées depuis le scrapping.

### tfidf
Pour les résultats des tfidf calculés

### projections
Pour enregistrer des projections effectuées.

## Membres
BRUNEAU Vincent  
MARI Micky
