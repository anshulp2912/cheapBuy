import os
import sys
sys.path.append(os.path.abspath('../../'))
from cheapBuy.code.web_scrappers.web_scrapper import scrapper

def test_scrapper_bjs_result():
    result = scrapper("https://www.bjs.com/product/brita-pour-through-pitcher-replacement-filter-10-pk/23578")
    assert result is not None

def test_scrapper_bjs_result_len():
    result = scrapper("https://www.bjs.com/product/brita-pour-through-pitcher-replacement-filter-10-pk/23578")
    assert len(result) == 4