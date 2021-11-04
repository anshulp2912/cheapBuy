"""
Copyright (c) 2021 Anshul Patel
This code is licensed under MIT license (see LICENSE.MD for details)

@author: cheapBuy
"""

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from web_scrappers.FetchDescription import FetchDescription
from web_scrappers.WebScrapper_Amazon import WebScrapper_Amazon
from web_scrappers.WebScrapper_Bjs import WebScrapper_Bjs
from web_scrappers.WebScrapper_Ebay import WebScrapper_Ebay
from web_scrappers.WebScrapper_Costco import WebScrapper_Costco
from web_scrappers.WebScrapper_Walmart import WebScrapper_Walmart

class WebScrapper:
    
    def __init__(self,product_link):
        self.product_link = product_link
    
    def get_driver(self):
        options = webdriver.ChromeOptions()
        # options.binary_location = '/usr/bin/chromium-browser'
        options.add_argument("--no-sandbox") #This make Chromium reachable
        options.add_argument("--no-default-browser-check") #Overrides default choices
        options.add_argument("--no-first-run")
        options.add_argument("--disable-default-apps") 
        driver = webdriver.Chrome(options=options, executable_path=ChromeDriverManager().install())
        return driver

    def get_description(self):
        if 'walmart' in self.product_link:
            source = 'walmart'
            fd = FetchDescription(self.product_link)
            description = fd.fetch_desc_walmart()
        elif 'amazon' in self.product_link:
            source = 'amazon'
            fd = FetchDescription(self.product_link)
            description = fd.fetch_desc_amazon()
        elif 'ebay' in self.product_link:
            source = 'ebay'
            fd = FetchDescription(self.product_link)
            description = fd.fetch_desc_ebay()
        elif 'costco' in self.product_link:
            source = 'costco'
            fd = FetchDescription(self.product_link)
            description = fd.fetch_desc_costco()
        elif 'bjs' in self.product_link:
            source= 'bjs'
            fd = FetchDescription(self.product_link)
            description = fd.fetch_desc_bjs()
        else:
            source = 'N/A'
        if source != 'N/A':
            return description
    
    def call_scrapper(self):
        product_description = self.get_description()
        print(product_description)
        
        t_amazon = WebScrapper_Amazon(product_description)
        t_walmart = WebScrapper_Walmart(product_description)
        t_ebay = WebScrapper_Ebay(product_description)
        t_bjs = WebScrapper_Bjs(product_description)
        t_costco = WebScrapper_Costco(product_description)
        
        t_amazon.start()
        t_walmart.start()
        t_ebay.start()
        t_bjs.start()
        t_costco.start()
        
        t_amazon.join()
        t_walmart.join()
        t_ebay.join()
        t_bjs.join()
        t_costco.join()
        
        results_amazon = t_amazon.result
        results_walmart = t_walmart.result
        results_ebay = t_ebay.result
        results_bjs = t_bjs.result
        results_costco = t_costco.result
        
        return [results_amazon, results_walmart, results_ebay, results_bjs, results_costco]

#link = 'https://www.walmart.com/ip/Brita-Longlast-Water-Filter-Replacement-Reduces-Lead-2-Count/128876038'
#link = 'https://www.walmart.com/ip/Brita-Longlast-Water-Filter-Replacement-Reduces-Lead-2-Count/128876038'
#ws = WebScrapper(link)
#result=ws.call_scrapper()        