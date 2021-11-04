cheapBuy Phase 2 - Improved Version<br><br>
Motivation:<br><br>
cheapBuy Extension provides you ease to buy any product through your favourite websites like Amazon, Walmart, Ebay, Bjs, Costco, etc, by providing prices of the same product from all different websites. It takes a lot of time to search for the same product in different websites, and find the cheapest one, instead just add our extension cheapBuy and it will automatically fetch you price of the same product from different websites and you can directly compare the prices from different websites through our extension. In sum, cheapBuy is a one stop solution to buy the cheapest product online.
<br><br>
Features - Price Comparison, Get alternative websites for the products, highlights cheapest product.
<br><br>
Which users use this?
Everyone who buys products online from famous online websites can use this to compare prices for any product they wish to buy.
<br><br>
Steps for Execution:
<br><br>
Code Functionalities:
<br><br>
1. web_scraper.py 
○ function get_driver(): Returns a chrome instance using the Selenium webdriver. 
○ function scrapper(link): Checks which ecommerce platform the link(parameter of function) belongs to and searches for details of similar products on amazon and ebay. Details include description, price and url. This function returns these details as a dictionary. 
<br><br>
2. web_scrapper_amazon.py 
○ function get_url_amazon(search_term): This function returns the Amazon url of the product (search_term) given as an argument. 
○ function scrap_amazon(driver, search_term) Webpage of the product corresponding to search_term is retrieved using BeautifulSoup and Selenium chrome web driver. 
○ function extract_item_amazon(driver, search_term) Extracts the product description, price , URL and website name (“Amazon”) best corresponding to search_term and returns it through a dictionary variable.
<br><br> 
3. web_scrapper_bjs.py 
○ function get_url_bjs(search_term) This function returns the url corresponding to the BJS website for the product (search_term) given as an argument. 
○ function scrap_bjs(driver, search_term) Webpage of the product corresponding to search_term is retrieved using BeautifulSoup and Selenium chrome web driver. 
○ function extract_item_bjs(driver, search_term) Extracts the product description, price , URL and website name (“BJS”) best corresponding to search_term and returns it through a dictionary variable. 
<br><br>
4. web_scrapper_ebay.py 
○ function get_url_ebay(search_term) This function returns the url corresponding to the eBay website for the product (search_term) given as an argument. 
○ function scrap_ebay(driver, search_term) Webpage of the product corresponding to search_term is retrieved using BeautifulSoup and Selenium chrome web driver. 
○ function extract_item_ebay(driver, search_term) Extracts the product description, price , URL and website name (“EBay”) best corresponding to search_term and returns it through a dictionary variable.
<br><br> 
5.web_scrapper_walmart.py 
○ function get_url_walmart(search_term) This function returns the url corresponding to the walmart website for the product (search_term) given as an argument. 
○ function scrap_walmart(driver, search_term) Webpage of the product corresponding to search_term is retrieved using BeautifulSoup and Selenium chrome web driver. 
○ function extract_item_walmart(driver, search_term) Extracts the product description, price , URL and website name (“Walmart”) best corresponding to search_term and returns it through a dictionary variable.
<br><br>
6.WebScrapper_Costco.py
<br><br>
7. FetchDescription.py
<br><br>


