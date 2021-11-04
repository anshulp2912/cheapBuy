# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 23:52:22 2021

@author: Rohan Shah
"""

import sys
sys.path.append('../')
from source.web_scrappers.FetchDescription import FetchDescription

def test_fetch_description_ebay():
    link = "https://www.ebay.com/itm/274922036305?epid=25014370331&hash=item4002a15c51:g:v8UAAOSwsv1hKB7z"
    fd = FetchDescription(link)
    assert fd.fetch_desc_ebay() == "3x Brita Longlast Water Filter Replacement  - NEW Sealed"

