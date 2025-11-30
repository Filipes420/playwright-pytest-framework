from pages.main_page import MainPage
from pages.products_page import ProductsPage
from pages.product_page import ProductPage
from conftest import setup
from pages.base_page import BasePage

def test_verify_all_products_and_product_detail_page(setup):
    ## classes
    base_page = BasePage(setup)

    main_page = MainPage(setup)

    products_page = ProductsPage(setup)

    product_page = ProductPage(setup)

    #main page
    main_page.click_products()

    ## products page
    assert base_page.get_title() == "Automation Exercise - All Products"
    assert products_page.get_products_header() == "ALL PRODUCTS"

    assert products_page.get_products_count() == 34

    ## checks if all products are visible with relevant information (img, price tag, price)
    products_page.verify_all_products()

    products_page.click_view_product()

    # product page
    assert base_page.get_title() == "Automation Exercise - Product Details"

    assert product_page.get_product_name() == "Blue Top"
    assert product_page.get_product_category() == "Category: Women > Tops"
    assert product_page.get_product_price() == "Rs. 500"
    assert product_page.get_product_availability() == "Availability: In Stock"
    assert product_page.get_product_condition() == "Condition: New"
    assert product_page.get_product_brand() == "Brand: Polo"


