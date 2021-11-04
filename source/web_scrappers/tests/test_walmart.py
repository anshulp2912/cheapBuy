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
description = 'Brita Longlast Water Filter Replacement Reduces Lead 2 Count'

template = 'https://www.walmart.com/search?q={}'
search_term = description.replace(' ','+')
url = template.format(search_term)

#url = get_url_walmart()
driver.get(url)
soup = BeautifulSoup(driver.page_source,"html.parser")
#mb1 ph1 pa0-x1 bb b--near-white w-25
results = soup.find_all('div',{'class': 'flex flex-wrap w-100 flex-grow-0 flex-shrink-0 ph2 pr0-xl pl4-xl mt0-xl mt3'})
print('results:{}'.format(results))

result={}
#results = scrap_walmart()
if len(results) == 0:
    print(result) 
item=results[0]
atag = item.find("a",{"class":"absolute w-100 h-100 z-1"})
result['description'] = (atag.find("span",{"class":"w_DJ"})).text
result['url'] = atag.get('href')
parent_price= item.find("div",{"class":"flex flex-wrap justify-start items-center lh-title mb2 mb1-m"})
result['price'] = parent_price.find("div", {"class":"b black f5 mr1 mr2-xl lh-copy f4-l"}).text.strip('$')
result['site'] = 'walmart'
