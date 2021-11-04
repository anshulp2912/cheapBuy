"""
Copyright (c) 2021 Anshul Patel
This code is licensed under MIT license (see LICENSE.MD for details)

@author: cheapBuy
"""

import sys
sys.path.append('../')
from code.webscrappers.WebScrapper_Bjs import WebScrapper_Bjs

def test_bjs_scrapper():
    
    description = 'brita pour through pitcher replacement filter 10 pk'
    t = WebScrapper_Bjs(description)
    t.start()
    t.join()
    assert t.result == {'description': 'Brita Pour-Through Pitcher Replacement Filter, 10 pk.',
     'url': 'https://tinyurl.com/yfgukkgl',
     'price': '$39.99 ',
     'site': 'bjs'}