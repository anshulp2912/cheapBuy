import os
import sys
sys.path.append(os.path.abspath('../../'))
from cheapBuy.code.web_scrappers.web_scrapper import scrapper


def test_scrapper_amazon_result():
    result = scrapper("https://www.amazon.com/2021-Apple-10-2-inch-iPad-Wi-Fi/dp/B09G9FPHY6/ref=sr_1_3?dchild=1&keywords=ipad&qid=1632940310&sr=8-3")
    assert result is not None

def test_scrapper_amazon_result_len():
    result = scrapper(
        "https://www.amazon.com/Sony-X950H-75-Inch-Compatibility/dp/B0846NF2B4/ref=sr_1_1_sspa?crid=3H3ARH8C75Q2Q&dchild=1&keywords=sony+bravia+65+inch&qid=1633023125&sprefix=sony+br%2Caps%2C162&sr=8-1-spons&psc=1&smid=A2K7RN1DSQCI9O&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyT0pDOVdFNFRBQzRQJmVuY3J5cHRlZElkPUEwMDIxOTI2MVhSMlJIVktFTE5DSSZlbmNyeXB0ZWRBZElkPUEwNTAwNTIyMVc0TFlBRU9aSTFOQSZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU=")
    assert len(result) == 4

def test_scrapper_amazon_result_description_count():
    result = scrapper(
        "https://www.amazon.com/NexiGo-Playstation-Console-Controller-Charging/dp/B08QHG53MP/ref=sr_1_1_sspa?dchild=1&keywords=ps4&qid=1633023315&s=electronics&sr=1-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUE1N0FZRVcxUjZMUk4mZW5jcnlwdGVkSWQ9QTA4Nzc3OTQxMEEyVDJZS0xFTVhRJmVuY3J5cHRlZEFkSWQ9QTA4OTQ4MjYzTlo1OUpTQVJFTlJLJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ==")
    assert len(result["description"]) == 1

def test_scrapper_amazon_result_site_ebay():
    result = scrapper(
        "https://www.amazon.com/Apple-iPhone-12-64GB-Blue/dp/B08PNM1LNZ/ref=sr_1_1?dchild=1&keywords=iphone12&qid=1633023388&s=electronics&sr=1-1")
    assert result["site"] == ["ebay"]

def test_scrapper_amazon_result_url_ebay():
    result = scrapper(
        "https://www.amazon.com/OnePlus-Buds-Ear-Comfortable-Lightweight/dp/B08K9YT25X/ref=sr_1_3?dchild=1&keywords=oneplus+buds&qid=1633023431&s=electronics&sr=1-3")
    assert result["url"][0].find("ebay") != -1
