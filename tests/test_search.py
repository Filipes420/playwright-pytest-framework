import pytest

from conftest import setup
from pages.main_page import MainPage
from pages.base_page import BasePage
from pages.products_page import ProductsPage
from data.data_generator import get_random_product
from data.data_generator import get_random_product_word


def test_search_product(setup):
    main_page = MainPage(setup)
    products_page = ProductsPage(setup)
    header = main_page.get_header()

    # navigate to products page
    header.click_products()

    #get random product from csv
    expected_product = get_random_product()

    # search by product name
    products_page.search_product(expected_product["name"])

    #verify search heading
    assert products_page.get_products_header() == "searched products"

    # collect all found products
    found_products = products_page.get_product_cards()

    for product in found_products:
        #verify product name
        assert product.get_product_name() == expected_product["name"]

        #verify product price
        assert product.get_product_price() == expected_product["price"]

        #verify product image loaded
        assert product.is_product_image_loaded() == True


def test_search_products(setup):
    main_page = MainPage(setup)
    products_page = ProductsPage(setup)
    header = main_page.get_header()

    # navigate to products page
    header.click_products()

    # get random word from product names from csv
    search_word = get_random_product_word()

    # search by random product word
    products_page.search_product(search_word)

    # verify search heading
    assert products_page.get_products_header() == "searched products"

    # collect all found products
    found_products = products_page.get_product_cards()

    for product in found_products:
        assert search_word in product.get_product_name()


