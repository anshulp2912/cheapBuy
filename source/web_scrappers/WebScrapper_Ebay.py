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

class WebScrapper_Ebay(Thread):
    
    def __init__(self,description):
        self.driver = self.get_driver()
        self.description = description
        self.result = {}
        super(WebScrapper_Ebay,self).__init__()
        
    def run(self):
        self.result={}
        try:
            results = self.scrap_ebay()
            if len(results) == 0:
                self.result = {}
                print('Ebay_results empty')
            else:
                item=results[0]
                atag = item.find("a",{"class":"s-item__link"})
                self.result['description'] = item.find("h3",{"class":"s-item__title"}).get_text().strip()
                self.result['url'] = atag.get('href')
                self.result['url'] = shorten_url(self.result['url'])
                self.result['price'] = item.find("span",{"class":"s-item__price"}).get_text().strip()
                self.result['site'] = 'ebay'
        except:
            print('Ebay_results exception')
            self.result = {}
        
    def get_driver(self):
        options = webdriver.ChromeOptions()
        #options.headless = True
        driver = webdriver.Chrome(options=options, executable_path=ChromeDriverManager().install())
        return driver
    
    def get_url_ebay(self):
      try:
          template="https://www.ebay.com"+"/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw={}"
          template=template.format(self.description)
      except:
          template = ''
      return template

    def scrap_ebay(self):
        results = []
        try:
            url = self.get_url_ebay()
            self.driver.get(url)
            soup = BeautifulSoup(self.driver.page_source, 'html.parser')
            results = soup.find_all("li",{"class":"s-item s-item__pl-on-bottom s-item--watch-at-corner"})
        except:
            results = []
        return results
