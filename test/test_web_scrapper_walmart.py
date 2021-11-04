import os
import sys
sys.path.append(os.path.abspath('../../'))
from cheapBuy.code.web_scrappers.web_scrapper_walmart import scrap_walmart, get_url_walmart
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def setup_get_driver_details():
    options = webdriver.ChromeOptions()
    options.headless = True
    driver = webdriver.Chrome(options=options, executable_path=ChromeDriverManager().install())
    return driver


def test_get_url_walmart_1():
    item_name = "SAMSUNG Galaxy Tab A7 32GB"
    assert get_url_walmart(item_name) == "https://www.walmart.com/search?q=SAMSUNG+Galaxy+Tab+A7+32GB"


def test_get_url_walmart_2():
    assert get_url_walmart("Brita Longlast Replacement Filters Dispensers") == "https://www.walmart.com/search?q=Brita+Longlast+Replacement+Filters+Dispensers"


def test_scrap_walmart():
    item_name = "Fresh Strawberries, 1 lb"
    results = scrap_walmart(setup_get_driver_details(), item_name)
    assert results is not None
