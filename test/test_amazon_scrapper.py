"""
Copyright (c) 2021 Anshul Patel
This code is licensed under MIT license (see LICENSE.MD for details)

@author: cheapBuy
"""

import sys
sys.path.append('../')
from code.web_scrappers.WebScrapper_Amazon import WebScrapper_Amazon

def test_amazon_scrapper():
    
    description = 'Brita 35503 Standard Replacement Filters'
    t = WebScrapper_Amazon(description)
    t.start()
    t.join()
    assert t.result == {'description': 'Sapphire Water Filters compatible with Sapphire, Brita and Pur Pitchers, 6-Pack',
     'url': 'https://tinyurl.com/yjy52tsm',
     'price': '$27.95',
     'site': 'amazon'}
