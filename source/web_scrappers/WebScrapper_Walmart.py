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


class WebScrapper_Walmart(Thread):
    """
    Main class used to scrape results from Walmart
    
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
    get_url_walmart:
        Returns walmart URL
    scrap_walmart:
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
        super(WebScrapper_Walmart,self).__init__()
        
    def run(self):
        """ 
        Returns final result
        """
        self.result={}
        try:
        	#Get results from scrapping function
            results = self.scrap_walmart()
            #Condition to check whether results are avialable or not
            if len(results) == 0:
                self.result = {} 
                print('Walmart_results empty')
            else:
                item=results[0]
                #Find teh atag containing our required item
                atag = item.find("a",{"class":"absolute w-100 h-100 z-1"})
                #Extract description from the atag
                self.result['description'] = (atag.find("span",{"class":"w_DJ"})).text
                #Get the URL for the page and shorten it
                self.result['url'] = shorten_url(self.result['url'])
                self.result['url'] = atag.get('href')
                #Find the parent div containging price of the item
                parent_price= item.find("div",{"class":"flex flex-wrap justify-start items-center lh-title mb2 mb1-m"})
                #Find the price of the item
                self.result['price'] = parent_price.find("div", {"class":"b black f5 mr1 mr2-xl lh-copy f4-l"}).text
                #Assign the site as walmart to result
                self.result['site'] = 'walmart'
        except:
            print('Walmart_results exception')
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
        
    def get_url_walmart(self):
        """ 
        Returns walmart URL
        """
    	#Prepare URL for given description
        template = 'https://www.walmart.com/search?q={}'
        search_term = self.description.replace(' ','+')
        return template.format(search_term)

    def scrap_walmart(self):
        """ 
        Returns Scraped result
        """
    	#Call the function to get URL
        url = self.get_url_walmart()
        #Assign the URL to driver
        self.driver.get(url)
        #Use BeautifulSoup to scrap the webpage
        soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        results = soup.find_all('div',{'class': 'h-100 pb1-xl pr4-xl pv1 ph1'})
        return results

    
