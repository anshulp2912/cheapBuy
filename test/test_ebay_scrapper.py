"""
Copyright (c) 2021 Anshul Patel
This code is licensed under MIT license (see LICENSE.MD for details)

@author: cheapBuy
"""

import sys
sys.path.append('../')
from code.web_scrappers.WebScrapper_Ebay import WebScrapper_Ebay

def test_ebay_scrapper():
    
    description = '3x Brita Longlast Water Filter Replacement  - NEW Sealed'
    t = WebScrapper_Ebay(description)
    t.start()
    t.join()
    assert t.result == {'description': '3x Brita Longlast Water Filter Replacement  - NEW Sealed',
     'url': 'https://tinyurl.com/yg7pognr',
     'price': '$20.00',
     'site': 'ebay'}