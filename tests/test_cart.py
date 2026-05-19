import pytest

from pages.main_page import MainPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.product_page import ProductPage
from data.data_generator import get_random_product, get_random_cipher_integer

## expected test data across tests
expected_cart_modal_header = "Added!"
expected_cart_modal_body = "Your product has been added to cart."
expected_cart_labels = ["Item", "Description", "Price", "Quantity", "Total", ""]


def test_add_to_cart_without_quantity(empty_cart):

    # classes
    main_page = MainPage(empty_cart)
    products_page = ProductsPage(empty_cart)
    cart_page = CartPage(empty_cart)
    header = main_page.get_header()

    # set expected products data
    expected_products = [{"name": "Blue Top", "price": "500", "quantity": "1"},
                         {"name": "Men Tshirt", "price": "400", "quantity": "1"}]

    # navigate to products page
    header.click_products()

    ## cycle to search, verify and add to cart expected products
    for i, expected_product in enumerate(expected_products):

        #search product on products page
        products_page.search_product(expected_product["name"])

        # get product from products page
        actual_product = products_page.get_product_cards()

        # verify search found only one product
        assert len(actual_product) == 1

        actual_product = actual_product[0]

        # verify product details from products page
        assert actual_product.get_product_name() == expected_product["name"]
        assert actual_product.get_product_price() == expected_product["price"]
        assert actual_product.is_product_image_loaded()

        # add product to cart
        actual_product.click_add_to_cart()

        ## get cart_modal
        cart_modal = products_page.get_cart_modal()

        # verify cart modal
        assert cart_modal.get_header() == expected_cart_modal_header
        assert cart_modal.get_body() == expected_cart_modal_body

        # condition to determine whether to stay on page or go to cart
        if i == 1:
            cart_modal.click_view_cart()

        else:
            cart_modal.click_continue()

    # get cart from cart page
    cart = cart_page.get_cart()

    #get, verify cart header
    cart_labels = cart.get_cart_header_labels()
    assert len(expected_cart_labels) == len(cart_labels)
    for expected_cart_label in expected_cart_labels:
        assert expected_cart_label in cart_labels


    # get, verify cart products
    cart_products = cart.get_cart_products()
    assert len(expected_products) == len(cart_products)
    for expected_product in expected_products:
        assert expected_product in cart_products




def test_add_to_cart_with_quantity(empty_cart):

    main_page = MainPage(empty_cart)
    products_page = ProductsPage(empty_cart)
    cart_page = CartPage(empty_cart)
    product_page = ProductPage(empty_cart)
    header = main_page.get_header()

    # set expected products data
    expected_products = [{"name": "Blue Top", "price": "500", "quantity": "3"},
                         {"name": "Men Tshirt", "price": "400", "quantity": "2"}]

    header.click_products()


    ## cycle to search, verify and add to cart expected products
    for i, expected_product in enumerate(expected_products):

        # search product on products page
        products_page.search_product(expected_product["name"])

        # get product from products page
        actual_product = products_page.get_product_cards()

        # verify search found only one product
        assert len(actual_product) == 1

        actual_product = actual_product[0]

        # verify product details from products page
        assert actual_product.get_product_name() == expected_product["name"]
        assert actual_product.get_product_price() == expected_product["price"]
        assert actual_product.is_product_image_loaded()

        # click view product
        actual_product.click_view_product()

        # set product quantity on product page
        product_page.set_product_quantity(expected_product["quantity"])
        product_page.click_add_to_cart_button()

        ## get cart_modal
        cart_modal = product_page.get_cart_modal()

        # verify cart modal
        assert cart_modal.get_header() == expected_cart_modal_header
        assert cart_modal.get_body() == expected_cart_modal_body

        # condition to determine whether to stay on page or go to cart
        if i == 1:
            cart_modal.click_view_cart()

        else:
            cart_modal.click_continue()
            empty_cart.go_back()

    ## get cart from cart page
    cart = cart_page.get_cart()

    #get, verify cart header
    cart_labels = cart.get_cart_header_labels()
    assert len(expected_cart_labels) == len(cart_labels)
    for expected_cart_label in expected_cart_labels:
        assert expected_cart_label in cart_labels

    # get, verify cart products
    cart_products = cart.get_cart_products()
    assert len(expected_products) == len(cart_products)
    for expected_product in expected_products:
        assert expected_product in cart_products





