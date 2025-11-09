""" cartographie.py """

import pandas as pd
from sklearn.decomposition import PCA
import plotly.express as px

def projec_pca_interactive(datas, X_tfidf) -> None:
    """ Crée une projection PCA interactive des commentaires agrégés par recette. """

    # Reconstruction des textes par recette dans le même ordre que X_tfidf
    groupes = {}
    for _, (text, recipe_id, _, _) in datas.items():
        groupes.setdefault(recipe_id, []).append(text)

    # Pour hover, on concatène tous les commentaires d'une recette
    comments_by_recipe = [";".join(texts) for recipe_id, texts in groupes.items()]

    # Calcul de la PCA
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X_tfidf.toarray()) # pylint:disable=invalid-name

    # Création du DataFrame
    df = pd.DataFrame({
        'x': X_pca[:,0],
        'y': X_pca[:,1],
        'comment': comments_by_recipe
    })

    # Scatter interactif
    fig = px.scatter(
        df, x='x', y='y',
        hover_name='comment',
        hover_data={'x': False, 'y': False},
        title='Projection PCA interactive des commentaires de marmiton.org'
    )

    # Sauvegarde interactive en HTML
    fig.write_html("projection_pca_interactive.html")
    print("Carte interactive sauvegardée sous 'projection_pca_interactive.html'")