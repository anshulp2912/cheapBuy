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
description = 'Brita Filter'

template = "https://www.costco.com"+"/CatalogSearch?dept=All&keyword={}"
search_term = description.replace(' ','+')
url = template.format(search_term)

driver.get(url)
soup = BeautifulSoup(driver.page_source,"html.parser")
#mb1 ph1 pa0-x1 bb b--near-white w-25
results = soup.find_all('div',{'class': 'product-list grid'})
print('results:{}'.format(results))

result={}
#results = scrap_walmart()
if len(results) == 0:
    print(result) 
item=results[0]
atag = item.find("span",{"class":"description"}).find('a')
result['description'] = atag.text
result['url'] = atag.get('href')
result['price'] = item.find("div",{"class":"price"}).text.strip()
result['site'] = 'costco'
