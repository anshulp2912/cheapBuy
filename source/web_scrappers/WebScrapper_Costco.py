"""
Copyright (c) 2021 Anshul Patel
This code is licensed under MIT license (see LICENSE.MD for details)

@author: cheapBuy
"""

from bs4 import BeautifulSoup
from threading import Thread
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

import sys
sys.path.append('../')
from source.utils.url_shortener import shorten_url

class WebScrapper_Costco(Thread):
    """
    Main class used to scrape results from Costco
    
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
    get_url_costco:
        Returns costco URL
    scrap_costco:
        Returns Scraped result
    """
    
    def __init__(self,description):
        """
        Parameters
        ----------
        description : str
            description of the product
        """
        self.driver = self.get_driver()
        if len(description)<5:
            self.description = description
        else:
            self.description = ' '.join(description.split()[:5])
        self.result = {}
        super(WebScrapper_Costco,self).__init__()
       
    def run(self):
        self.result={}
        try:
            results = self.scrap_costco()
            if len(results) == 0:
                print('Costco_results empty')
                self.result={}
            else:                
                item=results[0]
                atag = item.find("span",{"class":"description"}).find('a')
                self.result['description'] = atag.text
                self.result['url'] = atag.get('href')
                self.result['url'] = shorten_url(self.result['url'])
                self.result['price'] = item.find("div",{"class":"price"}).text.strip()
                self.result['site'] = 'costco'
        except:
            print('Costco_results exception')
            self.result={}
            
    def get_driver(self):
        options = webdriver.ChromeOptions()
        options.headless = True
        driver = webdriver.Chrome(options=options, executable_path=ChromeDriverManager().install())
        return driver
    
    def get_url_costco(self):
        template = "https://www.costco.com"+"/CatalogSearch?dept=All&keyword={}"
        search_term = self.description.replace(' ','+')
        return template.format(search_term)

    def scrap_costco(self):
        url = self.get_url_costco()
        self.driver.get(url)
        soup = BeautifulSoup(self.driver.page_source,"html.parser")
        results = soup.find_all('div',{'class': 'product-list grid'})
        return results
        

