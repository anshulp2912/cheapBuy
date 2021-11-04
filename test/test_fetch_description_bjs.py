import os
import sys
sys.path.append(os.path.abspath('../../'))
from cheapBuy.code.web_scrappers.fetch_description_bjs import description_from_url_bjs

def test_fetch_description_bjs1():
    link = "https://www.bjs.com/product/apple-ipad-pro-11-3rd-generation-256gb-wi-fi---space-gray/3000000000001510763"
    assert description_from_url_bjs(link) == "apple ipad pro 11 3rd generation 256gb wi fi   space gray"

def test_fetch_description_bjs2():
    link = "https://www.bjs.com/product/brita-pour-through-pitcher-replacement-filter-10-pk/23578"
    description = description_from_url_bjs(link)
    assert description == "brita pour through pitcher replacement filter 10 pk"

