import os
import sys
sys.path.append(os.path.abspath('../../../'))
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from cheapBuy.code.web_scrappers.web_scrapper_amazon import extract_item_amazon
from cheapBuy.code.web_scrappers.web_scrapper_ebay import extract_item_ebay
from cheapBuy.code.web_scrappers.web_scrapper_walmart import extract_item_walmart
from cheapBuy.code.web_scrappers.fetch_description_amazon import description_from_url_amazon
from cheapBuy.code.web_scrappers.fetch_description_ebay import description_from_url_ebay
from cheapBuy.code.web_scrappers.fetch_description_walmart import description_from_url_walmart
from cheapBuy.code.web_scrappers.fetch_description_costco import description_from_url_costco
from cheapBuy.code.web_scrappers.fetch_description_bjs import description_from_url_bjs

def get_driver():
	options = webdriver.ChromeOptions()
	options.headless = True
	driver = webdriver.Chrome(options=options, executable_path=ChromeDriverManager().install())
	return driver

def scrapper(link):
	results = {'url':[],'description':[],'price':[],'site':[]}
	try:
		driver = get_driver()
		if 'amazon' in link:
			try:
				description = description_from_url_amazon(link)
				result_dict_ebay = extract_item_ebay(driver, description)
				results['url'].append(result_dict_ebay['url'])
				results['description'].append(result_dict_ebay['description'])
				results['price'].append(result_dict_ebay['price'])
				results['site'].append(result_dict_ebay['site'])
			except:
				results = {'url':[],'description':[],'price':[],'site':[]}
		elif 'ebay' in link:
			try:
				description = description_from_url_ebay(link)
				result_dict_amazon = extract_item_amazon(driver, description)
				results['url'].append(result_dict_amazon['url'])
				results['description'].append(result_dict_amazon['description'])
				results['price'].append(result_dict_amazon['price'])
				results['site'].append(result_dict_amazon['site'])
			except:
				results = {'url':[],'description':[],'price':[],'site':[]}
		elif 'walmart' in link:
			try:
				description = description_from_url_walmart(link)
				result_dict_amazon = extract_item_amazon(driver, description)
				result_dict_ebay = extract_item_ebay(driver, description)
				results['url'].append(result_dict_amazon['url'])
				results['url'].append(result_dict_ebay['url'])
				results['description'].append(result_dict_amazon['description'])
				results['description'].append(result_dict_ebay['description'])
				results['price'].append(result_dict_amazon['price'])
				results['price'].append(result_dict_ebay['price'])
				results['site'].append(result_dict_amazon['site'])
				results['site'].append(result_dict_ebay['site'])
			except:
				results = {'url':[],'description':[],'price':[],'site':[]}
		elif 'costco' in link:
			try:
				description = description_from_url_costco(link)
				result_dict_amazon = extract_item_amazon(driver, description)
				result_dict_ebay = extract_item_ebay(driver, description)
				results['url'].append(result_dict_amazon['url'])
				results['url'].append(result_dict_ebay['url'])
				results['description'].append(result_dict_amazon['description'])
				results['description'].append(result_dict_ebay['description'])
				results['price'].append(result_dict_amazon['price'])
				results['price'].append(result_dict_ebay['price'])
				results['site'].append(result_dict_amazon['site'])
				results['site'].append(result_dict_ebay['site'])
			except:
				results = {'url':[],'description':[],'price':[],'site':[]}
		else:
			try:
				description = description_from_url_bjs(link)
				result_dict_amazon = extract_item_amazon(driver, description)
				result_dict_ebay = extract_item_ebay(driver, description)
				results['url'].append(result_dict_amazon['url'])
				results['url'].append(result_dict_ebay['url'])
				results['description'].append(result_dict_amazon['description'])
				results['description'].append(result_dict_ebay['description'])
				results['price'].append(result_dict_amazon['price'])
				results['price'].append(result_dict_ebay['price'])
				results['site'].append(result_dict_amazon['site'])
				results['site'].append(result_dict_ebay['site'])
			except:
				results = {'url':[],'description':[],'price':[],'site':[]}
	except:
		results = {'url':[],'description':[],'price':[],'site':[]}

	return results