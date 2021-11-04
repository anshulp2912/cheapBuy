# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 23:52:22 2021

@author: Rohan Shah
"""

import sys
sys.path.append('../')
from code.web_scrappers.FetchDescription import FetchDescription

def test_fetch_description_costco():
    link = "https://www.costco.com/brita-replacement-filters%2c-10-pack.product.100131571.html"
    fd = FetchDescription(link)
    assert fd.fetch_desc_costco() == "brita replacement filters%2c 10 pack"
    
