# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 00:27:27 2021

@author: Rohan Shah
"""

from source.utils.url_shortener import shorten_url

def test_url_shortener():
    url = 'https://www.walmart.com/ip/Brita-Longlast-Water-Filter-Replacement-Reduces-Lead-2-Count/128876038'
    s_url = shorten_url(url)
    assert 'tinyurl.com' in s_url