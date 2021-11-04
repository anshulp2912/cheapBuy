"""
Copyright (c) 2021 Anshul Patel
This code is licensed under MIT license (see LICENSE.MD for details)

@author: cheapBuy
"""

from bs4 import BeautifulSoup

class WebScrapper_Ebay():
    
    def __init__(self,driver,description):
        self.driver = driver
        self.description = description
        
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
            print(url)
            soup = BeautifulSoup(self.driver.page_source, 'html.parser')
            results = soup.find_all("li",{"class":"s-item s-item__pl-on-bottom s-item--watch-at-corner"})
        except:
            results = []
        return results

    def extract_item_ebay(self):
        result={}
        try:
            results = self.scrap_ebay()
            print(results)
            if len(results) == 0:
                return result 
            item=results[0]
            atag = item.find("a",{"class":"s-item__link"})
            result['description'] = item.find("h3",{"class":"s-item__title"}).get_text().strip()
            result['url'] = atag.get('href')
            result['price'] = item.find("span",{"class":"s-item__price"}).get_text().strip().strip('$')
            result['site'] = 'ebay'
        except:
            result = {}
        return result