from conftest import setup
from pages.main_page import MainPage
from pages.products_page import ProductsPage

def test_scrap_data(setup):

    main_page = MainPage(setup)
    products_page = ProductsPage(setup)

    main_page.click_products()
    products_page.scrap_product_data()
