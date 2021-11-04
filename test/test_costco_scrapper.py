"""
Copyright (c) 2021 Anshul Patel
This code is licensed under MIT license (see LICENSE.MD for details)

@author: cheapBuy
"""

import sys
sys.path.append('../')
from code.webscrappers.WebScrapper_Costco import WebScrapper_Costco

def test_costco_scrapper():
    
    description = 'brita replacement filters%2c 10 pack'
    t = WebScrapper_Costco(description)
    t.start()
    t.join()
    assert t.result == {'description': 'Brita Replacement Filters, 10-pack\n\t\t\t',
     'url': 'https://tinyurl.com/yfznxg8z',
     'price': '$39.99',
     'site': 'costco'}