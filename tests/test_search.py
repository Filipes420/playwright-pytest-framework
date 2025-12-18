from conftest import setup
from pages.main_page import MainPage
from pages.base_page import BasePage
from pages.products_page import ProductsPage
from data.data_generator import get_random_product
from data.data_generator import get_random_product_word

def test_search_product(setup):
    base_page = BasePage(setup)
    main_page = MainPage(setup)
    products_page = ProductsPage(setup)

    ## main page
    main_page.click_products()

    ## products page
    assert base_page.get_title() == "Automation Exercise - All Products"

    product_data = get_random_product()

    products_page.search_product(product_data["name"])
    assert products_page.get_searched_products_header() == "SEARCHED PRODUCTS"
    products_page.verify_searched_products(product_data["name"], product_data["price"])

def test_search_products(setup):
    base_page = BasePage(setup)
    main_page = MainPage(setup)
    products_page = ProductsPage(setup)

    ## main page
    main_page.click_products()

    ## products page
    assert base_page.get_title() == "Automation Exercise - All Products"

    search_word = get_random_product_word()
    products_page.search_product(search_word)
    assert products_page.get_searched_products_header() == "SEARCHED PRODUCTS"
    products_page.verify_searched_products(search_word)

