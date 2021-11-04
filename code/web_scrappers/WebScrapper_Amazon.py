"""
Copyright (c) 2021 Anshul Patel
This code is licensed under MIT license (see LICENSE.MD for details)

@author: cheapBuy
"""

from bs4 import BeautifulSoup

class WebScrapper_Amazon():
    
    def __init__(self,driver,description):
        self.driver = driver
        self.description = description
    
    def get_url_amazon(self):
    	try:
    		template = 'https://www.amazon.com'+'/s?k={}&ref=nb_sb_ss_ts-doa-p_3_5'
    		search_term = self.description.replace(' ','+')
    		template = template.format(search_term)
    	except:
    		template = ''
    	return template

    def scrap_amazon(self):
    	results=[]
    	try:
    		url = self.get_url_amazon()
    		self.driver.get(url)
    		soup = BeautifulSoup(self.driver.page_source, 'html.parser')
    		results = soup.find_all('div',{'data-component-type': 's-search-result'})
    	except:
    		results = []
    	return results


    def extract_item_amazon(self):
    	result={}
    	try:
    		results = self.scrap_amazon()
    		if len(results) == 0:
    			return result
    		item=results[0]
    		atag = item.h2.a
    		result['description'] = atag.text.strip()
    		result['url'] = 'https://www.amazon.com'+atag.get('href')
    		price_parent = item.find('span', 'a-price')
    		result['price'] = price_parent.find('span', 'a-offscreen').text
    		result['site'] = 'amazon'
    	except:
    		result={}
    	return result

