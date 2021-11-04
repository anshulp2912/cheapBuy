"""
Copyright (c) 2021 Anshul Patel
This code is licensed under MIT license (see LICENSE.MD for details)

@author: cheapBuy
"""

from bs4 import BeautifulSoup

class WebScrapper_Walmart():
    
    def __init__(self,driver,description):
        self.driver = driver
        self.description = description
        
    def get_url_walmart(self):
        template = 'https://www.walmart.com/search?q={}'
        search_term = self.description.replace(' ','+')
        return template.format(search_term)

    def scrap_walmart(self):
        url = self.get_url_walmart()
        self.driver.get(url)
        soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        results = soup.find_all('div',{'class': 'h-100 pb1-xl pr4-xl pv1 ph1'})
        print('results:{}'.format(results))
        return results

    def extract_item_walmart(self):
        result={}
        results = self.scrap_walmart()
        if len(results) == 0:
            return result 
        item=results[0]
        atag = item.find("a",{"class":"absolute w-100 h-100 z-1"})
        result['description'] = (atag.find("span",{"class":"w_DJ"})).text
        result['url'] = atag.get('href')
        parent_price= item.find("div",{"class":"flex flex-wrap justify-start items-center lh-title mb2 mb1-m"})
        result['price'] = parent_price.find("div", {"class":"b black f5 mr1 mr2-xl lh-copy f4-l"}).text.strip('$')
        result['site'] = 'walmart'
        return result
