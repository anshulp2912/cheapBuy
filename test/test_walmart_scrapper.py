"""
Copyright (c) 2021 Anshul Patel
This code is licensed under MIT license (see LICENSE.MD for details)

@author: cheapBuy
"""

import sys
sys.path.append('../')
from source.web_scrappers.WebScrapper_Walmart import WebScrapper_Walmart

def test_walmart_scrapper():
    
    description = 'Brita Longlast Water Filter Replacement Reduces Lead 2 Count'
    t = WebScrapper_Walmart(description)
    t.start()
    t.join()
    assert t.result == {'description': 'Sapphire Water Filters compatible with Sapphire, Brita and Pur Pitchers, 6-Pack',
     'url': 'https://tinyurl.com/yjy52tsm',
     'price': '$27.95',
     'site': 'amazon'}