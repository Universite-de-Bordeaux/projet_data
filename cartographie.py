""" cartographie.py """

import pandas as pd
from sklearn.decomposition import PCA
import plotly.express as px

def projec_pca_interactive(datas, X_tfidf, filename="projection_pca_interactive.html", clusters=None) -> None:
    """ Crée une projection PCA interactive des commentaires agrégés par recette. """

    # Calcul de la PCA
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X_tfidf.toarray()) # pylint:disable=invalid-name

    # Base du dataframe
    data = {
        'x': X_pca[:, 0],
        'y': X_pca[:, 1],
        'comment': datas
    }

    # Si clusters
    if clusters is not None:
        data['cluster'] = clusters

    # Création du DataFrame
    df = pd.DataFrame(data)

    if clusters is not None:
        df['cluster'] = df['cluster'].astype(str)

    # Scatter interactif
    fig = px.scatter(
        df, x='x', y='y',
        color='cluster' if clusters is not None else None,
        color_discrete_sequence=px.colors.qualitative.Plotly,
        hover_name='comment',
        hover_data={'x': False, 'y': False},
        title='Projection PCA interactive des commentaires de marmiton.org'
    )

    # Sauvegarde interactive en HTML
    fig.write_html(filename)
    print(f"Carte interactive sauvegardée sous {filename}")
