import requests


def test_post_result():
    result = requests.post("http://3.89.74.154:8080/scrap?link=https://www.bjs.com/product/brita-pour-through-pitcher-replacement-filter-6-pk/23538")
    assert result is not None
