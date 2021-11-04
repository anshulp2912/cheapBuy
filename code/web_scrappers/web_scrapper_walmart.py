from bs4 import BeautifulSoup

def get_url_walmart(search_term):
    template = 'https://www.walmart.com/search?q={}'
    search_term = search_term.replace(' ','+')
    return template.format(search_term)

def scrap_walmart(driver, search_term):
    url = get_url_walmart(search_term)
    driver.get(url)
    soup = BeautifulSoup(driver.page_source)
    results = soup.find_all('div',{'class': 'flex flex-wrap w-100 flex-grow-0 flex-shrink-0 ph2 pr0-xl pl4-xl mt0-xl mt3'})
    print('results:{}'.format(results))
    return results

def extract_item_walmart(driver, search_term):
    result={}
    results = scrap_walmart(driver, search_term)
    if len(results) == 0:
        return result 
    item=results[0]
    atag = item.find("a",{"class":"absolute w-100 h-100 z-1"})
    result['description'] = atag.find("span",{"class":"w_Cs"}).text
    result['url'] = atag.get('href')
    parent_price= item.find("div",{"class":"flex flex-wrap justify-start items-center lh-title mb2 mb1-m"})
    result['price'] = parent_price.find("div", {"class":"b black f5 mr1 mr2-xl lh-copy f4-l"}).text.strip('$')
    result['site'] = 'walmart'
    return result

