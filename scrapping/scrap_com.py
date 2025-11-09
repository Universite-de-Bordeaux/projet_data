""" Récupération des commentaires des recettes Marmiton """
# pylint: disable=line-too-long

from concurrent.futures import ThreadPoolExecutor
from selenium import webdriver
from bs4 import BeautifulSoup

from .const import MAX_WORKERS, MAX_SLUG

def scrap_com(url:str)->list[str]:
    """ Scrap les commentaires d'une recette Marmiton à partir de son URL """
    driver = webdriver.Chrome()
    driver.get(url)

    soup = BeautifulSoup(driver.page_source, "html.parser")
    coms = soup.find_all("p", class_="recipe-reviews-list__review__text")
    comments = [com.get_text().strip() for com in coms]

    driver.quit()
    return comments

def scrap_comments(urls:str|list[str], nb_url:int = MAX_SLUG, nb_workers:int = MAX_WORKERS)->list[str]:
    """ Scrap les commentaires d'une recette Marmiton à partir de son URL ou d'une liste d'URLs """
    if isinstance(urls, str):
        return scrap_com(urls)

    urls = urls[:min(nb_url, len(urls))]

    comments = []
    # Lancement du scrapping en parallèle
    with ThreadPoolExecutor(max_workers=nb_workers) as executor:
        results = executor.map(scrap_com, urls)

    # Fusion des commentaires
    for com_list in results:
        comments += com_list

    print(f"Scrapping terminé pour {len(urls)} recettes.")
    return comments
