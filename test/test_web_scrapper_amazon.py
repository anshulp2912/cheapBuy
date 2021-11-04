import os
import sys
sys.path.append(os.path.abspath('../../'))
from cheapBuy.code.web_scrappers.web_scrapper_amazon import scrap_amazon, get_url_amazon
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def setup_get_driver_details():
    options = webdriver.ChromeOptions()
    options.headless = True
    driver = webdriver.Chrome(options=options, executable_path=ChromeDriverManager().install())
    return driver


def test_get_url_amazon_1():
    item_name = "2021 Apple 10 2 inch iPad Wi Fi"
    assert get_url_amazon(item_name) == "https://www.amazon.com/s?k=2021+Apple+10+2+inch+iPad+Wi+Fi&ref=nb_sb_ss_ts-doa-p_3_5"


def test_get_url_amazon_2():
    assert get_url_amazon("Brita Longlast Replacement Filters Dispensers") == "https://www.amazon.com/s?k=Brita+Longlast+Replacement+Filters+Dispensers&ref=nb_sb_ss_ts-doa-p_3_5"


def test_scrap_amazon():
    item_name = "W. Trends Sunset Twin-Size Metal Bunk Bed - Black"
    results = scrap_amazon(setup_get_driver_details(), item_name)
    assert results is not None
