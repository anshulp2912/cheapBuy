import os
import sys
sys.path.append(os.path.abspath('../../'))
from cheapBuy.code.web_scrappers.web_scrapper import get_driver

def test_get_driver():
    assert get_driver() is not None