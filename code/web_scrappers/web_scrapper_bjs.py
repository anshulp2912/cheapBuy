from bs4 import BeautifulSoup

def get_url_bjs(search_term):
  template="https://www.bjs.com"+"/search/{}"
  return template.format(search_term)

def scrap_bjs(driver, search_term):
  url = get_url_bjs(search_term)
  driver.get(url)
  soup = BeautifulSoup(driver.page_source, 'html.parser')
  results = soup.find_all("div",{"class":"each-section"})
  return results

def extract_item_bjs(driver, search_term):
  result={}
  results = scrap_bjs(driver, search_term)
  if len(results) == 0:
    return result 
  item=results[1]
  atag = item.find("a",{"class":"product-link mt-xl-3 mt-xs-3 mt-md-0 mt-3"})
  result['url'] = 'https://www.bjs.com'+atag.get('href')
  result['description'] = item.find("h2",{"class":"product-title no-select d-none"})
  if(result['description']==None):
    result['description']=item.find("h2",{"class":"product-title no-select d-none d-sm-block"}).get_text().strip()
  else:
    result['description']=result['description'].get("title")
  result['description']=result['description'].replace(" | safeHtml","")
  result['price'] = item.find("div",{"class":"price-block no-select"}).get_text().strip().strip('$')
  result['site'] = 'bjs'
  return result

