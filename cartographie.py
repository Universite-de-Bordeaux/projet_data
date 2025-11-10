""" cartographie.py """

import pandas as pd
from sklearn.decomposition import PCA
import plotly.express as px

def projec_pca_interactive(datas, X_tfidf, filename="projection_pca_interactive.html") -> None:
    """ Crée une projection PCA interactive des commentaires agrégés par recette. """

    # Calcul de la PCA
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X_tfidf.toarray()) # pylint:disable=invalid-name

    # Création du DataFrame
    df = pd.DataFrame({
        'x': X_pca[:,0],
        'y': X_pca[:,1],
        'comment': datas
    })

    # Scatter interactif
    fig = px.scatter(
        df, x='x', y='y',
        hover_name='comment',
        hover_data={'x': False, 'y': False},
        title='Projection PCA interactive des commentaires de marmiton.org'
    )

    # Sauvegarde interactive en HTML
    fig.write_html(filename)
    print(f"Carte interactive sauvegardée sous {filename}")