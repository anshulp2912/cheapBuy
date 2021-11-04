import os
import sys
sys.path.append(os.path.abspath('../../'))
from cheapBuy.code.web_scrappers.web_scrapper import scrapper


def test_scrapper_costco_result():
    result = scrapper("https://www.costco.com/brita-replacement-filters%2c-10-pack.product.100131571.html")
    assert result is not None

def test_scrapper_costco_result_len():
    result = scrapper("https://www.costco.com/brita-replacement-filters%2c-10-pack.product.100131571.html")
    assert len(result) == 4