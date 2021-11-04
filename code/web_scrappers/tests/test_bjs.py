"""
Copyright (c) 2021 Anshul Patel
This code is licensed under MIT license (see LICENSE.MD for details)

@author: cheapBuy
"""

import os
import sys
sys.path.append(os.path.abspath('../../../'))
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from bs4 import BeautifulSoup

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options, executable_path=ChromeDriverManager().install())
description = 'Brita Longlast Water Filter Replacement'

template = "https://www.bjs.com"+"/search/{}"
search_term = description.replace(' ','+')
url = template.format(search_term)

driver.get(url)
soup = BeautifulSoup(driver.page_source,"html.parser")
results = soup.find_all('div',{'class': 'products-list'})
# if '<!-- -->' in str(results[0]):
#     results = soup.find_all('div',{'class': 'ngucarousel-items'})
print('results:{}'.format(results))

result={}
if len(results) == 0:
    print(result) 
item=results[1]
atag = item.find("a",{"class":"product-link mt-xl-3 mt-xs-3 mt-md-0 mt-3"})
result['description'] = (atag.find("h2",{"class":"product-title no-select d-none"})).text
result['url'] = "www.bjs.com" + str(atag.get('href'))
result['price'] = item.find("div",{"class":"display-price"}).find('span',{'class':'price'}).text
result['site'] = 'bjs'
