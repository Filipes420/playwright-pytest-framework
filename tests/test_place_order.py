from data.data_generator import get_random_product
from data.data_generator import get_random_cipher_integer
from conftest import empty_cart
from pages.checkout_page import CheckOutPage
from pages.main_page import MainPage
from pages.payment_page import PaymentPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage

def test_place_order(empty_cart):

    ## classes
    main_page = MainPage(empty_cart)
    products_page = ProductsPage(empty_cart)
    cart_page = CartPage(empty_cart)
    checkout_page = CheckOutPage(empty_cart)
    payment_page = PaymentPage(empty_cart)

    ## go to products page
    main_page.click_products()

    ## add random amount of products to cart

    order_products = products_page.add_multiple_products_to_cart(get_random_cipher_integer())

    ## go to cart page
    products_page.click_cart_button()

    ## verify cart page
    cart_page.verify_cart(order_products)

    # click proceed
    cart_page.click_proceed_button()

    # verify delivery information
    checkout_page.verify_delivery_information()

    #verify order (cart)
    checkout_page.verify_cart_header()

    #click place order
    checkout_page.click_place_order_button()

    #fill out card details
    payment_page.fill_out_card_details_form()

    ##place order
    payment_page.submit_order()









