# cheapBuy Phase 2 - Improved Version<br><br>
**Motivation:**<br><br>
cheapBuy Extension provides you ease to buy any product through your favourite websites like Amazon, Walmart, Ebay, Bjs, Costco, etc, by providing prices of the same product from all different websites. It takes a lot of time to search for the same product in different websites, and find the cheapest one, instead just add our extension cheapBuy and it will automatically fetch you price of the same product from different websites and you can directly compare the prices from different websites through our extension. In sum, cheapBuy is a one stop solution to buy the cheapest product online.
<br><br>
**Features** - Price Comparison, Get alternative websites for the products, highlights cheapest product.
<br><br>
**Which users use this?**
Everyone who buys products online from famous online websites can use this to compare prices for any product they wish to buy.
<br><br>
**Steps for Execution:**
<br><br>
1. Clone the github repository at the preferable location in your local machine. You will need git to be preinstalled in the system. Once the repository is cloned in your system, with the help of cd command ,
```
git clone https://github.com/anshulp2912/cheapBuy.git
cd cheapBuy
```
2. This project uses Python 3, so make sure that [Python](https://www.python.org/downloads/) and [Pip](https://pip.pypa.io/en/stable/installation/) are preinstalled. All requirements of the project are listed in the ```requirements.txt``` file. Use pip to install all of the requirements.
```
pip install -r requirements.txt
```
3. Check out the demo video to know about the use of the website in the media files.
4. To locally run the streamlit website, we would recommend setting up an Anaconda Environment and running the command
```
streamlit run cheapBuy_user_interface.py
```
**Code Functionalities:**
<br><br>
**web_scrappers**
1. **FetchDescription.py**
<br><br>
* function fetch_desc_walmart():The function fetch_desc_walmart fetches description from the incoming walmart URL.<br>
* function fetch_desc_amazon(): The function fetch_desc_amazon fetches description from the incoming amazon URL.<br>
* function fetch_desc_ebay(): The function fetch_desc_ebay fetches description from the incoming ebay URL.<br>
* function fetch_desc_costco(): The function fetch_desc_costco fetches description from the incoming costco URL.<br>
* function fetch_desc_bjs(): The function fetch_desc_bjs fetches description from the incoming bjs URL.<br>
<br><br><br>
2. **WebScrapper.py**
* function get_description(): The function get_description checks website of incoming URL and calls the respective website function to fetch the description.<br>
* function call_scrapper(): The function call_scrapper utilizes threads to call scrapper functions for all 5 websites and get the final result.<br><br>
3. **WebScrapper_Amazon.py** <br><br>
* function run(): The function run is executed when the thread is started. It gets result from function scrap_amazon and extracts output in desired format from the result<br>
* function get_driver(): The function get_driver prepares and returns a Chrome driver using Selenium.<br>
* function get_url_amazon(): The function get_url_amazon prepares a URL for Amazon scraping from description.<br>
* function scrap_amazon(): The function scrap_amazon performs web scraping using BeautifulSoup on the URL provided by function get_url_amazon.
<br><br> 
4. **WebScrapper_Bjs.py** <br><br>
* function run(): The function run is executed when the thread is started. It gets the result from the function scrap_bjs and extracts output in the desired format from the result.<br>
* function get_driver(): The function get_driver prepares and returns a Chrome driver using Selenium.<br>
* function get_url_bjs(): The function get_url_bjs prepares a URL for Bjs scraping from description.<br>
* function scrap_bjs(): The function scrap_bjs performs web scraping using BeautifulSoup on the URL provided by function get_url_bjs.<br>
<br><br>
5. **WebScrapper_Costco.py**<br><br>
* function run(): The function run is executed when the thread is started. It gets the result from the function scrap_costco and extracts output in the desired format from the result.<br>
* function get_driver(): The function get_driver prepares and returns a Chrome driver using Selenium.<br>
* function get_url_costco(): The function get_url_costco prepares a URL for Costco scraping from description.<br>
* function scrap_costco(): The function scrap_costco performs web scraping using BeautifulSoup on the URL provided by function get_url_costco.
<br><br> 
6. **WebScrapper_Ebay.py** <br><br>
* function run(): The function run is executed when the thread is started. It gets the result from the function scrap_ebay and extracts output in the desired format from the result.<br>
* function get_driver(): The function get_driver prepares and returns a Chrome driver using Selenium.<br>
* function get_url_ebay(): The function get_url_ebay prepares a URL for Ebay scraping from description.<br>
* function scrap_ebay(): The function scrap_ebay performs web scraping using BeautifulSoup on the URL provided by function get_url_ebay.
<br><br>
7. **WebScrapper_Walmart.py** <br><br>
* function run(): The function run is executed when the thread is started. It gets the result from the function scrap_walmart and extracts output in the desired format from the result<br>
* function get_driver(): The function get_driver prepares and returns a Chrome driver using Selenium.<br>
* function get_url_walmart(): The function get_url_walmart prepares a URL for Walmart scrapping from description<br>
* function scrap_walmart(): The function scrap_walmart performs web scraping using BeautifulSoup on the URL provided by function get_url_walmart.<br>
<br><br>

**extension**
1. **index.html**<br>
Default page of an extension that opens when the extension is clicked.<br><br>
2. **main.css**<br>
This cascading style sheet (CSS) file provides format and style for the contents of the extension display.<br><br>
3. **manifest.json**<br>
Config file of an extension that provides important information regarding the extension.<br><br>
4. **popup.js**<br>
This popup.js file fetches the url of the current tab and passes it to the server. The response is generated from the server which fetches the same product from different websites and displays it on the extension.<br><br>
5. **robot.txt**<br>
A robots.txt file tells search engine crawlers which URLs the crawler can access on your site.<br><br>

**Output:**<br>
The below screenshot shows the website created for cheapBuy. In the output, the cheapest option is highlighted in the website.<br><br>
<img src="https://github.com/anshulp2912/cheapBuy/blob/main/media/UIinterface.png"><br><br>
<img src="https://github.com/anshulp2912/cheapBuy/blob/main/media/CheapBuy_Extension.PNG"><br><br>
<img src="https://github.com/anshulp2912/cheapBuy/blob/main/media/CheapBuy_Extension_output.PNG"><br><br>
<img src="https://github.com/anshulp2912/cheapBuy/blob/main/media/highlight.jpeg"><br><br>
