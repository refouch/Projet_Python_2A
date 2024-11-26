import sys 
sys.path.append("code/")

import unittest 
import scraping 

class Test_scraping(unittest.TestCase):
    def test_scraping_pays(self):
        url = https://fr.wikipedia.org/wiki/L%C3%A9gislation_sur_le_cannabis
        table = scrape_first_table(url)
        data, header = table_to_list(table)
        data_pays = make_pandas(data, header)

        self.assertEqual(data_pays.shape, (87,5))
        self.assertEqual(data_pays.iat[0,1], "Illégale")


if __name__ == '__main__':
    unittest.main()