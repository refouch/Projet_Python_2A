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

def make_rows(table):
    """Fonction prenant le tableau au format html pour le diviser dans une liste 
        Chaque item de la liste correspond alors à une ligne du tableau
        Args: table (bs4 element)
        Return: rows (list)
    """
    result = []

    # Pour le corps du tableau
    body = table.find("tbody")
    rows = body.find_all("tr")
    for row in rows:
        cols = row.find_all("td")
        cols = [ele.text.strip() for ele in cols]
        result.append(cols)

    return result

def make_pandas(rows):
    dictionnaire = dict()
    for row in rows:
        if len(row) > 0:
            dictionnaire[row[0]] = row[1:]
        print(dictionnaire)

    data_pays = pd.DataFrame.from_dict(dictionnaire, orient="index")

    return data_pays
        
table = scrape_first_table(url)
rows = make_rows(table)
data_pays = make_pandas(rows)

print(data_pays.head())

#---------------------------------------- RESTE A FAIRE --------------------------------------------
# -
# IMPLEMENTER UN BOUT DE CODE POUR RECUPERER LES EN TÊTE ET LES INTEGRER AU PANDA
# SUPPRIMER LA DERNIERE LIGNE DU TABLEAU SUR LES NOTES
# TIDY LES DONNEES ET PRENDRE DES DECISIONS SUR COMMENT REPRESENTER CHAQUE VARIABLE
# + EVENTUELLEMENT MERGE CA AVEC LES DONNES EUROPEENNES.