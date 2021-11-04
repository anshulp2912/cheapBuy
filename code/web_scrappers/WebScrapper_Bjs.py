"""
Copyright (c) 2021 Anshul Patel
This code is licensed under MIT license (see LICENSE.MD for details)

@author: cheapBuy
"""

from bs4 import BeautifulSoup

class WebScrapper_Bjs():
    
    def __init__(self,driver,description):
        self.driver = driver
        if len(description)<5:
            self.description = description
        else:
            self.description = ' '.join(description.split()[:5])
    
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

    def extract_item_bjs(self):
        results = self.scrap_bjs()
        result={}
        if len(results) == 0:
            print(result) 
        item=results[1]
        atag = item.find("a",{"class":"product-link mt-xl-3 mt-xs-3 mt-md-0 mt-3"})
        result['description'] = (atag.find("h2",{"class":"product-title no-select d-none"})).text
        result['url'] = "www.bjs.com" + str(atag.get('href'))
        result['price'] = item.find("div",{"class":"display-price"}).find('span',{'class':'price'}).text
        result['site'] = 'bjs'
        return result

