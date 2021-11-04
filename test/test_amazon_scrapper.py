"""
Copyright (c) 2021 Anshul Patel
This code is licensed under MIT license (see LICENSE.MD for details)

@author: cheapBuy
"""

import sys
sys.path.append('../')
from source.web_scrappers.WebScrapper_Amazon import WebScrapper_Amazon

def test_amazon_scrapper():
    
    description = 'Brita 35503 Standard Replacement Filters'
    t = WebScrapper_Amazon(description)
    t.start()
    t.join()
    assert t.result is not None
