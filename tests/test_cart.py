import pytest
from pages.main_page import MainPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.product_page import ProductPage
from data.data_generator import get_random_product, get_random_cipher_integer


def test_add_to_cart_without_quantity(empty_cart):

    main_page = MainPage(empty_cart)
    products_page = ProductsPage(empty_cart)
    cart_page = CartPage(empty_cart)

    main_page.click_products()

    product1 = get_random_product()
    product1["quantity"] = "1"

    product2 = get_random_product()
    product2["quantity"] = "1"

    # verify product 1 and add to cart
    products_page.search_product(product1["name"])
    products_page.verify_searched_products(product1["name"], product1["price"])
    products_page.add_to_cart()
    products_page.verify_added_to_cart_popup()

    # verify product 2, add to cart go to cart
    products_page.search_product(product2["name"])
    products_page.verify_searched_products(product2["name"], product2["price"])
    products_page.add_to_cart()
    products_page.verify_added_to_cart_popup(True)

    ## create list of products
    products = [product1, product2]

    cart_page.verify_cart(products)
    cart_page.delete_all_cart_products()


def test_add_to_cart_with_quantity(empty_cart):
    main_page = MainPage(empty_cart)
    products_page = ProductsPage(empty_cart)
    cart_page = CartPage(empty_cart)
    product_page = ProductPage(empty_cart)

    main_page.click_products()

    # PRODUCT DATA GENERATION #

    product1 = get_random_product()
    product1["quantity"] = str(get_random_cipher_integer())

    product2 = get_random_product()
    product2["quantity"] = str(get_random_cipher_integer())

    # PRODUCT 1 ACTIONS #

    # search, verify and view product 1
    products_page.search_product(product1["name"])
    products_page.verify_searched_products(product1["name"], product1["price"])
    products_page.click_view_product()

    # set quantity, add to cart and verify added to cart modal

    product_page.set_product_quantity(product1["quantity"])
    product_page.click_add_to_cart_button()
    product_page.verify_added_to_cart_popup()

    product_page.click_products()

    # PRODUCT 2 ACTIONS #

    # verify product 2 and view product
    products_page.search_product(product2["name"])
    products_page.verify_searched_products(product2["name"], product2["price"])
    products_page.click_view_product()

    # set quantity, add to cart and verify added to cart modal

    product_page.set_product_quantity(product2["quantity"])
    product_page.click_add_to_cart_button()
    product_page.verify_added_to_cart_popup(True)



