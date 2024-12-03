# SCRAPING DE LA PAGE WIKIPEDIA SUR LA LEGALISATION DU CANNABIS
# -- https://fr.wikipedia.org/wiki/L%C3%A9gislation_sur_le_cannabis

import requests as rq
import bs4 as bs
import pandas as pd

url = "https://fr.wikipedia.org/wiki/L%C3%A9gislation_sur_le_cannabis"

def scrape_first_table(url):
    """ Fonction prenant en argument un lien wikipedia pour retourner le premier tableau de la page
        Arguments: url (str)
        Return: table (bs4 element)
    """
    request = rq.get(url)
    page = bs.BeautifulSoup(request.content, "lxml")
    table = page.find("table")
    return table

def table_to_list(table):
    """Fonction prenant le tableau au format html pour le diviser dans une liste 
        Chaque item de la liste correspond alors à une ligne du tableau. La liste "header" 
        rassembles les en-tête.
        Args: table (bs4 element)
        Return: data, header (list)
    """
    data = []
    header = []

    body = table.find("tbody")
    rows = body.find_all("tr")

    #Pour les en-tête:
    row = rows[0]
    cols = row.find_all("th")
    cols = [ele.text.strip() for ele in cols]
    header.append(cols)

    # Pour le corps du tableau:
    for row in rows[1:]:
        cols = row.find_all("td")
        cols = [ele.text.strip() for ele in cols]
        data.append(cols)

    return data, header

def make_pandas(data, header):
    """Fonction prenant le tableau sous forme de liste pour le transformer en dataset pandas
    à l'aide d'un dictionnaire.
    Arguments: data, header (list)
    Returns: data_pays (pandas dataset)"""

    dictionnaire = dict()
    for row in data:
        if len(row) > 0:
            dictionnaire[row[0]] = row[1:]

    data_pays = pd.DataFrame.from_dict(dictionnaire, orient="index")
    data_pays.columns = header[0][1:]

    return data_pays

#------------- PARTIE 2: Récupérer des informations sur le continent
# L'objectif est ensuite de pouvoir isoler seulement les pays européens.

def get_countries_url(table):
        body = table.find("tbody")
        rows = body.find_all("tr")
        result = []

        for row in rows[1:]:
            first_cell = row.find("td")
            links = first_cell.find_all("a")
            good_link = links[1].get("href")
            country = links[1].get("title")
            url_get_info = f"http://fr.wikipedia.org{good_link}"
            result.append({country: url_get_info})

        return result


#print(get_countries_url(scrape_first_table(url)))

# EN FAIT ON NE PEUT PAS TROUVER DE FACON CONSISTANTE LE CONTINENT A PARTIR D'UNE PAGE WIKI
# DONC IL VA FALLOIR TIDY TOUT CA A LA MAIN
# ON DISPOSE CEPENDANT DU CODE ISO 3316 QU'ON PEUT SCRAPER SUR LA PAGE DU PAYS = UNE PISTE A CREUSER POUR TIDY LES DONNEES APRES