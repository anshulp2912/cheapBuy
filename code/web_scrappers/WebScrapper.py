"""
Copyright (c) 2021 Anshul Patel
This code is licensed under MIT license (see LICENSE.MD for details)

@author: cheapBuy
"""
import os
import sys
sys.path.append(os.path.abspath('../../../'))
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
        #options.headless = True
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
        driver = self.get_driver()
        
        results_amazon = WebScrapper_Amazon(driver,product_description).extract_item_amazon()
        results_walmart = WebScrapper_Walmart(driver,product_description).extract_item_walmart()
        results_ebay = WebScrapper_Ebay(driver,product_description).extract_item_ebay()
        results_bjs = WebScrapper_Bjs(driver,product_description).extract_item_bjs()
        results_costco = WebScrapper_Costco(driver,product_description).extract_item_costco()

        return [results_amazon,results_walmart,results_ebay,results_bjs,results_costco]

#link = 'https://www.walmart.com/ip/Brita-Longlast-Water-Filter-Replacement-Reduces-Lead-2-Count/128876038'
#ws = WebScrapper(link)
#result=ws.call_scrapper()        