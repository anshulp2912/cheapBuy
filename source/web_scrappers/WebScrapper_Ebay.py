"""
Copyright (c) 2021 Anshul Patel
This code is licensed under MIT license (see LICENSE.MD for details)

@author: cheapBuy
"""

#Import libraries
from bs4 import BeautifulSoup
from threading import Thread
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from source.utils.url_shortener import shorten_url

#Set working directory path
import sys
sys.path.append('../')


class WebScrapper_Ebay(Thread):
    """
    Main class used to scrape results from Ebay
    
    ...

    Attributes
    ----------
    description : str
        description of the product
        
    Methods
    -------
    run:
        Threaded method to execute subclasses
    get_driver:
        Returns Chrome Driver
    get_url_ebay:
        Returns ebay URL
    scrap_ebay:
        Returns Scraped result
    """
    
    def __init__(self,description):
        """
        Parameters
        ----------
        description : str
            description of the product
        """
        #Initialize class variables
        self.driver = self.get_driver()
        self.description = description
        self.result = {}
        super(WebScrapper_Ebay,self).__init__()
        
    def run(self):
        """ 
        Returns final result
        """
        self.result={}
        try:
            #Get results from scrapping function
            results = self.scrap_ebay()
            #Condition to check whether results are avialable or not
            if len(results) == 0:
                self.result = {}
                print('Ebay_results empty')
            else:
                item=results[0]
                #Find teh atag containing our required item
                atag = item.find("a",{"class":"s-item__link"})
                #Extract description from the atag
                self.result['description'] = item.find("h3",{"class":"s-item__title"}).get_text().strip()
                #Get the URL for the page and shorten item
                self.result['url'] = atag.get('href')
                self.result['url'] = shorten_url(self.result['url'])
                #Find the price of the item
                self.result['price'] = item.find("span",{"class":"s-item__price"}).get_text().strip()
                #Assign the site as ebay to result
                self.result['site'] = 'ebay'
        except:
            print('Ebay_results exception')
            self.result = {}
        
    def get_driver(self):
        """ 
        Returns Chrome Driver
        """
        #Prepare driver for scrapping
        options = webdriver.ChromeOptions()
        options.headless = True
        driver = webdriver.Chrome(options=options, executable_path=ChromeDriverManager().install())
        return driver
    
    def get_url_ebay(self):
        """ 
        Returns ebay URL
        """
        try:
            #Prepare URL for given description
            template="https://www.ebay.com"+"/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw={}"
            template=template.format(self.description)
        except:
            template = ''
        return template

    def scrap_ebay(self):
        """ 
        Returns Scraped result
        """
        results = []
        try:
            #Call the function to get URL
            url = self.get_url_ebay()
            self.driver.get(url)
            #Use BeautifulSoup to scrap the webpage
            soup = BeautifulSoup(self.driver.page_source, 'html.parser')
            results = soup.find_all("li",{"class":"s-item s-item__pl-on-bottom s-item--watch-at-corner"})
        except:
            results = []
        return results
