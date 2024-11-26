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
        Chaque item de la liste correspond alors à une ligne du tableau
        Args: table (bs4 element)
        Return: rows (list)
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
    dictionnaire = dict()
    for row in data:
        if len(row) > 0:
            dictionnaire[row[0]] = row[1:]

    data_pays = pd.DataFrame.from_dict(dictionnaire, orient="index")
    data_pays.columns = header[0][1:]

    return data_pays
        
table = scrape_first_table(url)
data, header = table_to_list(table)
data_pays = make_pandas(data, header)

print(data_pays.head())

#---------------------------------------- RESTE A FAIRE --------------------------------------------
#
# SUPPRIMER LA DERNIERE LIGNE DU TABLEAU SUR LES NOTES
# TIDY LES DONNEES ET PRENDRE DES DECISIONS SUR COMMENT REPRESENTER CHAQUE VARIABLE
# + EVENTUELLEMENT MERGE CA AVEC LES DONNES EUROPEENNES.