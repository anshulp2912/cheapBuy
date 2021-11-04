import os
import sys
sys.path.append(os.path.abspath('../../'))
from cheapBuy.code.web_scrappers.web_scrapper_bjs import scrap_bjs, get_url_bjs
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def setup_get_driver_details():
    options = webdriver.ChromeOptions()
    options.headless = True
    driver = webdriver.Chrome(options=options, executable_path=ChromeDriverManager().install())
    return driver


def test_get_url_bjs_1():
    item_name = "Amazfit Band 5 Fitness Tracker with Alexa Built-in"
    assert get_url_bjs(item_name) == "https://www.bjs.com/search/Amazfit Band 5 Fitness Tracker with Alexa Built-in"


def test_get_url_bjs_2():
    assert get_url_bjs("Brita Longlast Replacement Filters Dispensers") == "https://www.bjs.com/search/Brita Longlast Replacement Filters Dispensers"


def test_scrap_bjs():
    item_name = "SAMSUNG Galaxy Tab A7 32GB"
    results = scrap_bjs(setup_get_driver_details(), item_name)
    assert results is not None
