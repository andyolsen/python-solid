from hamcrest import *
import pytest
from product import Product

product = None

@pytest.fixture(autouse=True)
def run_around_tests():
    global product
    product = Product("TV", 1500, 5, 4, 3, 5, 4, 3)
    yield

def test_product_taxPayable_correct():
    assert_that(product.taxPayable(), close_to(300, 0.1))

def test_product_ratings_containsRating():
    assert_that(product.ratings, has_item(3))

def test_product_ratings_doesntContainAbsentRating():
    assert_that(product.ratings, not(has_item(2)))