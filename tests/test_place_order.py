from data.data_generator import get_random_product
from data.data_generator import get_random_cipher_integer
from conftest import empty_cart
from pages.checkout_page import CheckOutPage
from pages.main_page import MainPage
from pages.payment_page import PaymentPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage


expected_cart_modal_header = "Added!"

expected_cart_modal_body = "Your product has been added to cart."

expected_cart_labels = ["Item", "Description", "Price", "Quantity", "Total", ""]

expected_products = [{"name": "Blue Top", "price": "500", "quantity": "1"},
                     {"name": "Men Tshirt", "price": "400", "quantity": "1"}]


expected_address = {"name": "Mr. Filip Gonda",
            "address1": "",
            "address2": "Vojkovce",
            "house_number":"30",
            "full_address": "Vojkovce Slovenská republika 05361",
            "state": "United States",
            "phone_number": "0950461967"
        }
def test_place_order(empty_cart):

    ## classes
    main_page = MainPage(empty_cart)
    products_page = ProductsPage(empty_cart)
    cart_page = CartPage(empty_cart)
    checkout_page = CheckOutPage(empty_cart)
    payment_page = PaymentPage(empty_cart)
    header = main_page.get_header()

    ## go to products page
    header.click_products()

    ## search expected products
    for i, expected_product in enumerate(expected_products):

        # search expected product
        products_page.search_product(expected_product["name"])

        # get product from products page
        actual_product = products_page.get_product_cards()

        # verify only one product was retrieved
        assert len(actual_product) == 1
        actual_product = actual_product[0]

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

    # go to checkout page
    cart_page.click_proceed_button()

    # verify delivery information
    address = checkout_page.get_delivery_address()
    assert address == expected_address

    # get cart
    cart = checkout_page.get_cart()

    # get, verify cart header
    cart_labels = cart.get_cart_header_labels()
    assert len(expected_cart_labels) == len(cart_labels)
    for expected_cart_label in expected_cart_labels:
        assert expected_cart_label in cart_labels

    # get, verify cart products
    cart_products = cart.get_cart_products()
    assert len(expected_products) == len(cart_products)
    for expected_product in expected_products:
        assert expected_product in cart_products

    # click place order
    checkout_page.click_place_order_button()

    # fill out card details
    payment_page.fill_out_card_details_form()

    # place order
    payment_page.submit_order()

    #download invoice
    payment_page.download_order_invoice()











