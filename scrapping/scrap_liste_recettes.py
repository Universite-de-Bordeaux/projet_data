""" Récupération des URLs des recettes à partir des sitemaps XML de Marmiton """
import xml.etree.ElementTree as ET
import requests

def get_all_recipe_slugs()->list[str]:
    """ Récupère les slugs des recettes depuis les sitemaps XML de Marmiton. """
    base = "https://www.marmiton.org/wsitemap_recipes_{}.xml"
    slugs = []

    for i in range(1, 10):
        sitemap_url = base.format(i)
        response = requests.get(sitemap_url, timeout=10)
        response.raise_for_status()

        root = ET.fromstring(response.content)
        for loc in root.findall(".//{*}loc"):
            url = loc.text
            if "recette_" in url:
                slug = url.split("recette_")[1].split(".aspx")[0]
                slugs.append(slug)

    return slugs
