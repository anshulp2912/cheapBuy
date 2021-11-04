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

class WebScrapper_Bjs(Thread):
    
    def __init__(self,description):
        self.driver = self.get_driver()
        if len(description)<5:
            self.description = description
        else:
            self.description = ' '.join(description.split()[:5])
        self.result = {}
        super(WebScrapper_Bjs,self).__init__()
    
    def run(self):
        try:
            results = self.scrap_bjs()
            self.result={}
            if len(results) == 0:
                print('BJs_results empty')
                self.result={}
            else:
                item=results[1]
                atag = item.find("a",{"class":"product-link mt-xl-3 mt-xs-3 mt-md-0 mt-3"})
                self.result['description'] = (atag.find("h2",{"class":"product-title no-select d-none"})).text
                self.result['url'] = "www.bjs.com" + str(atag.get('href'))
                self.result['url'] = shorten_url(self.result['url'])
                self.result['price'] = item.find("div",{"class":"display-price"}).find('span',{'class':'price'}).text
                self.result['site'] = 'bjs'
        except:
            print('BJs_results exception')
            self.result={}
            
    def get_driver(self):
        options = webdriver.ChromeOptions()
        options.headless = True
        driver = webdriver.Chrome(options=options, executable_path=ChromeDriverManager().install())
        return driver
    
    def get_url_bjs(self):
        template = "https://www.bjs.com"+"/search/{}"
        search_term = self.description.replace(' ','+')
        return template.format(search_term)

    def scrap_bjs(self):
        url = self.get_url_bjs()
        self.driver.get(url)
        soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        results = soup.find_all('div',{'class': 'products-list'})
        return results

        

