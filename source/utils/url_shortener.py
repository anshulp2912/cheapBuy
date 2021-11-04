"""
Copyright (c) 2021 Anshul Patel
This code is licensed under MIT license (see LICENSE.MD for details)

@author: cheapBuy
"""

# Import Libraries
from pyshorteners import Shortener 

def shorten_url(url):
    # Shorten the passed url
    s = Shortener()
    short_url = s.tinyurl.short(url)
    return short_url
