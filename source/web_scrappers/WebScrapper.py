"""
Copyright (c) 2021 Anshul Patel
This code is licensed under MIT license (see LICENSE.MD for details)

@author: cheapBuy
"""

#Import libraries
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from source.web_scrappers.FetchDescription import FetchDescription
from source.web_scrappers.WebScrapper_Amazon import WebScrapper_Amazon
from source.web_scrappers.WebScrapper_Bjs import WebScrapper_Bjs
from source.web_scrappers.WebScrapper_Ebay import WebScrapper_Ebay
from source.web_scrappers.WebScrapper_Costco import WebScrapper_Costco
from source.web_scrappers.WebScrapper_Walmart import WebScrapper_Walmart

class WebScrapper:
    """
    Main class used to fetch results by parsing the URL
    
    ...

    Attributes
    ----------
    product_link : str
        link of the product
        
    Methods
    -------
    get_driver:
        Returns Chrome Driver
    get_description:
        Fetch description for all websites
    call_scrapper:
        Build Threads and call scrapper for all websites
    """
    def __init__(self,product_link):
        """
        Parameters
        ----------
        product_link : str
            link of the product
        """
        self.product_link = product_link

    def get_description(self):
        """ 
        Fetch description for all websites
        """
        #Check the incoming URL for the website and call function to extract description accordingly
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
        """ 
        Build Threads and call scrapper for all websites
        """
        #Get description from incoming URL
        product_description = self.get_description()
        print(product_description)
        
        #Initialize thread for amazon scrapper
        t_amazon = WebScrapper_Amazon(product_description)
        #Initialize thread for walmart scrapper
        t_walmart = WebScrapper_Walmart(product_description)
        #Initialize thread for ebay scrapper
        t_ebay = WebScrapper_Ebay(product_description)
        #Initialize thread for bjs scrapper
        t_bjs = WebScrapper_Bjs(product_description)
        #Initialize thread for costco scrapper
        t_costco = WebScrapper_Costco(product_description)
        
        #Start thread for amazon
        t_amazon.start()
        #Start thread for walmart
        t_walmart.start()
        #Start thread for ebay
        t_ebay.start()
        #Start thread for bjs
        t_bjs.start()
        #Start thread for costco
        t_costco.start()
        
        #Join thread for amazon
        t_amazon.join()
        #Join thread for walmart
        t_walmart.join()
        #Join thread for ebay
        t_ebay.join()
        #Join thread for bjs
        t_bjs.join()
        #Join thread for costco
        t_costco.join()
        
        #Get results from the amazon thread
        results_amazon = t_amazon.result
        #Get results from the walmart thread
        results_walmart = t_walmart.result
        #Get results from the ebay thread
        results_ebay = t_ebay.result
        #Get results from the bjs thread
        results_bjs = t_bjs.result
        #Get results from the costco thread
        results_costco = t_costco.result
        
        return [results_amazon, results_walmart, results_ebay, results_bjs, results_costco]

#link = 'https://www.walmart.com/ip/Brita-Longlast-Water-Filter-Replacement-Reduces-Lead-2-Count/128876038'
#link = 'https://www.walmart.com/ip/Brita-Longlast-Water-Filter-Replacement-Reduces-Lead-2-Count/128876038'
#ws = WebScrapper(link)
#result=ws.call_scrapper()        
