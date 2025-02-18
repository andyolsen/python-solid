from hamcrest import *
from priceMatcher import valid_price
from product import Product


def test_product_validPrice_priceAccepted():
    product1 = Product("TV", 1500)
    assert_that(product1.price, valid_price())


def test_product_negativePrice_priceRejected():
    product2 = Product("TV", -1)
    assert_that(product2.price, is_not(valid_price()))


def test_product_tooExpensivePrice_priceRejected():
    product3 = Product("TV", 2501)
    assert_that(product3.price, is_not(valid_price()))