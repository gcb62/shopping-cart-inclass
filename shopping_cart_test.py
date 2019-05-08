# shopping_cart_test.py

import pytest

from shopping_cart import to_usd
from shopping_cart import now
from shopping_cart import product_match
# from shopping_cart import You_Pay



def test_usd():
    result1 = to_usd(3.5111111)
    result2 = to_usd(10)
    assert result1 == "$3.51"
    assert result2 == "$10.00"

def human_friendly_time():
    time1 = now(18.52)
    time2 = now(6.43)
    assert time1 == "18:52"
    assert time2 == "6:43"

def test_product_match():
    products = [
        {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
        {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    ]

    matching_product = product_match("2", products)
    assert matching_product["name"] == "All-Seasons Salt"

    with pytest.raises(IndexError):
        product_match("2222", products)

