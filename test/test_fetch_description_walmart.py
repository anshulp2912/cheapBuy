import os
import sys
sys.path.append(os.path.abspath('../../'))
from cheapBuy.code.web_scrappers.fetch_description_walmart import description_from_url_walmart


def test_fetch_description_walmart1():
    link = "https://www.walmart.com/ip/Oreo-Chocolate-Hazelnut-Flavored-Creme-Chocolate-Sandwich-Cookies-Family-Size-17-Oz/720352647"
    assert description_from_url_walmart(link) == "Oreo Chocolate Hazelnut Flavored Creme Chocolate Sandwich Cookies Family Size 17 Oz"

def test_fetch_description_walmart2():
    link = "https://www.walmart.com/ip/Time-and-Tru-Shaker-Cardigan/530065539"
    description = description_from_url_walmart(link)
    assert description == "Time and Tru Shaker Cardigan"
