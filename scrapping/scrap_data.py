""" Récupération des commentaires des recettes Marmiton """
# pylint: disable=line-too-long

from concurrent.futures import ThreadPoolExecutor
from selenium import webdriver
from bs4 import BeautifulSoup
from scrapping.const import SITE, AVIS, EXTENSION

from .const import MAX_WORKERS, MAX_SLUG

COMPTEUR = 0

def scrap_data_from_url(slug:str)->dict[int : str, str, str, str]:
    """ Scrap les commentaires d'une recette Marmiton à partir de son URL, 
    la page d'où elle provient, ainsi que le pseudo du commentateur """
    global COMPTEUR # pylint: disable=global-statement
    data = {}
    url = f"{SITE}{AVIS}{slug}{EXTENSION}"

    driver = webdriver.Chrome()
    driver.get(url)

    soup = BeautifulSoup(driver.page_source, "html.parser")
    coms = soup.find_all("div", class_="review__content")
    pseudos = soup.find_all("div", class_="review__author-pseudonyme")
    dates = soup.find_all("div", class_="review__date")

    print(f"Scrapping de la recette {slug} avec {len(coms)} commentaires.")
    for com, pseudo, date in zip(coms, pseudos, dates):
        data[COMPTEUR] = [com.get_text().strip(), slug, pseudo.get_text().strip(), date.get_text().strip()]
        COMPTEUR += 1
        print(COMPTEUR)

    driver.quit()
    return data

def scrap_data(slugs:str|list[str], nb_slug:int = MAX_SLUG, nb_workers:int = MAX_WORKERS)->list[str]:
    """ Scrap les commentaires d'une recette Marmiton à partir de son URL, 
    la page d'où elle provient, ainsi que le pseudo du commentateur 
     à partir de son URL ou d'une liste d'URLs """

    if isinstance(slugs, str):
        return scrap_data_from_url(slugs)

    slugs = slugs[:min(nb_slug, len(slugs))]

    data = {}
    # Lancement du scrapping en parallèle
    with ThreadPoolExecutor(max_workers=nb_workers) as executor:
        results = executor.map(scrap_data_from_url, slugs)

    # Fusion des commentaires
    for com_list in results:
        data.update(com_list)

    print(f"Scrapping terminé pour {len(slugs)} recettes.")
    return data
