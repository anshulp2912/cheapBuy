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


class WebScrapper_Amazon(Thread):
    """
    Main class used to scrape results from Amazon
    
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
    get_url_amazon:
        Returns amazon URL
    scrap_amazon:
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
        super(WebScrapper_Amazon,self).__init__()
    
    def run(self):
        """ 
        Returns final result
        """
        try:
            #Get results from scrapping function
            results = self.scrap_amazon()
            #Condition to check whether results are avialable or not
            if len(results) == 0:
                print('Amazon_results empty')
                self.result = {}
            else:
                item=results[0]
                #Find teh atag containing our required item
                atag = item.h2.a
                #Extract description from the atag
                self.result['description'] = atag.text.strip()
                #Get the URL for the page and shorten it
                self.result['url'] = 'https://www.amazon.com'+atag.get('href')
                self.result['url'] = shorten_url(self.result['url'])
                #Find the span containging price of the item
                price_parent = item.find('span', 'a-price')
                #Find the price of the item
                self.result['price'] = price_parent.find('span', 'a-offscreen').text
                #Assign the site as amazon to result
                self.result['site'] = 'amazon'
        except:
            print('Amazon_results exception')
            self.result={}

    def get_driver(self):
        """ 
        Returns Chrome Driver
        """
        #Prepare driver for scrapping
        options = webdriver.ChromeOptions()
        options.headless = True
        driver = webdriver.Chrome(options=options, executable_path=ChromeDriverManager().install())
        return driver
    
    def get_url_amazon(self):
        """ 
        Returns amazon URL
        """
        try:
            #Prepare URL for given description
            template = 'https://www.amazon.com'+'/s?k={}&ref=nb_sb_ss_ts-doa-p_3_5'
            search_term = self.description.replace(' ','+')
            template = template.format(search_term)
        except:
            template = ''
        return template

    def scrap_amazon(self):
        """ 
        Returns Scraped result
        """
        results=[]
        try:
            #Call the function to get URL
            url = self.get_url_amazon()
            self.driver.get(url)
            #Use BeautifulSoup to scrap the webpage
            soup = BeautifulSoup(self.driver.page_source, 'html.parser')
            results = soup.find_all('div',{'data-component-type': 's-search-result'})
        except:
            results = []
        return results
