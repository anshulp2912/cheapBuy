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
from utils.url_shortener import shorten_url

class WebScrapper_Walmart(Thread):
    
    def __init__(self,description):
        self.driver = self.get_driver()
        self.description = description
        self.result = {}
        super(WebScrapper_Walmart,self).__init__()
        
    def run(self):
        self.result={}
        try:
            results = self.scrap_walmart()
            if len(results) == 0:
                self.result = {} 
                print('Walmart_results empty')
            else:
                item=results[0]
                atag = item.find("a",{"class":"absolute w-100 h-100 z-1"})
                self.result['description'] = (atag.find("span",{"class":"w_DJ"})).text
                self.result['url'] = shorten_url(self.result['url'])
                self.result['url'] = atag.get('href')
                parent_price= item.find("div",{"class":"flex flex-wrap justify-start items-center lh-title mb2 mb1-m"})
                self.result['price'] = parent_price.find("div", {"class":"b black f5 mr1 mr2-xl lh-copy f4-l"}).text
                self.result['site'] = 'walmart'
        except:
            print('Walmart_results exception')
            self.result = {}
            
    def get_driver(self):
        options = webdriver.ChromeOptions()
        #options.headless = True
        driver = webdriver.Chrome(options=options, executable_path=ChromeDriverManager().install())
        return driver
        
    def get_url_walmart(self):
        template = 'https://www.walmart.com/search?q={}'
        search_term = self.description.replace(' ','+')
        return template.format(search_term)

    def scrap_walmart(self):
        url = self.get_url_walmart()
        self.driver.get(url)
        soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        results = soup.find_all('div',{'class': 'h-100 pb1-xl pr4-xl pv1 ph1'})
        return results

