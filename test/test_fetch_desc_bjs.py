"""
Copyright (c) 2021 Anshul Patel
This code is licensed under MIT license (see LICENSE.MD for details)

@author: cheapBuy
"""

import sys
sys.path.append('../')
from source.web_scrappers.FetchDescription import FetchDescription

def test_fetch_description_bjs():
    link = "https://www.bjs.com/product/brita-pour-through-pitcher-replacement-filter-10-pk/23578"
    fd = FetchDescription(link)
    assert fd.fetch_desc_bjs() == "brita pour through pitcher replacement filter 10 pk"
    
