"""
Copyright (c) 2021 Anshul Patel
This code is licensed under MIT license (see LICENSE.MD for details)

@author: cheapBuy
"""

from bs4 import BeautifulSoup

class WebScrapper_Costco():
    
    def __init__(self,driver,description):
        self.driver = driver
        if len(description)<5:
            self.description = description
        else:
            self.description = ' '.join(description.split()[:5])
    
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

    def extract_item_costco(self):
        result={}
        results = self.scrap_costco()
        if len(results) == 0:
            print(result) 
        item=results[0]
        atag = item.find("span",{"class":"description"}).find('a')
        result['description'] = atag.text
        result['url'] = atag.get('href')
        result['price'] = item.find("div",{"class":"price"}).text.strip()
        result['site'] = 'costco'
        return result

