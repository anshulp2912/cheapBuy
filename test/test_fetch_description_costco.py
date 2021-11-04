import os
import sys
sys.path.append(os.path.abspath('../../'))
from cheapBuy.code.web_scrappers.fetch_description_costco import description_from_url_costco


def test_fetch_description_costco1():
    link = "https://www.costco.com/brita-replacement-filters%2c-10-pack.product.100131571.html"
    assert description_from_url_costco(link) == "brita replacement filters%2c 10 pack"
