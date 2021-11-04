"""
Copyright (c) 2021 Anshul Patel
This code is licensed under MIT license (see LICENSE.MD for details)
@author: cheapBuy
"""

from bs4 import BeautifulSoup
import requests

class FetchDescription():
    """
    A class used to fetch description by parsing the URL
    
    ...
    Attributes
    ----------
    product_link : str
        link of the product
        
    Methods
    -------
    fetch_desc_walmart:
        Fetch description from Walmart
    fetch_desc_amazon:
        Fetch description from Amazon
    fetch_desc_ebay:
        Fetch description from Ebay
    fetch_desc_bjs:
        Fetch description from bjs
    fetch_desc_costco:
        Fetch description from Costco
    """


    
    def __init__(self,product_link):
        self.product_link = product_link
    
    def fetch_desc_walmart(self):
        description = ''
        try:
            link = self.product_link.replace("https://www.walmart.com/ip/","")
            for ch in link:
                if(ch!="/"):
                    description += ch
                else:
                    break
            description  = description.replace('-',' ')
        except:
            description = ''
        return description
    
    def fetch_desc_amazon(self):
        description = ''
        try:
            link = self.product_link.replace('https://www.amazon.com/','')
            for ch in link:
                if ch!='/':
                    description+=ch
                else:
                    break
            description = description.replace('-', ' ')
        except:
            description = ''
        return description
    
    def fetch_desc_ebay(self):
        try:
            html =  requests.get(self.product_link)
            soup=BeautifulSoup(html.content,'html.parser')
            product = soup.find("div",{"class" : "vi-swc-lsp"}, { "id" : "itemTitle" })
            title = product.find('span', class_="u-dspn").text.strip()
        except:
            title = ''
        return title 
    
    def fetch_desc_costco(self):
        description = ''
        try:
            link = self.product_link.replace("https://www.costco.com/","")
            for ch in link:
                if(ch!="."):
                    description += ch
                else:
                    break
            description  = description.replace('-',' ')
        except:
            description = ''
        return description
    
    def fetch_desc_bjs(self):
        description = ''
        try:
            link = self.product_link.replace("https://www.bjs.com/product/","")
            for ch in link:
                if(ch!="/"):
                    description += ch
                else:
                    break
            description  = description.replace('-',' ')
        except:
            description=''
        return description
    
