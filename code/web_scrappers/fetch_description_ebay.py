from bs4 import BeautifulSoup
import requests

def description_from_url_ebay(link):
	try:
		headers = {"user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"}
		html =  requests.get(link,headers=headers)
		soup=BeautifulSoup(html.content,'html.parser')
		product = soup.find("div",{"class" : "vi-swc-lsp"}, { "id" : "itemTitle" })
		title = product.find('span', class_="u-dspn").text.strip()
	except:
		title = ''
	return title 