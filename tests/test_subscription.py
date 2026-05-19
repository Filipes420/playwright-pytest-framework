from conftest import setup
from pages.main_page import MainPage
from pages.cart_page import CartPage
from data.data_generator import get_random_email

def test_subscription_home_page_positive(setup):
    main_page = MainPage(setup)

    # get random email that meets regex
    email = get_random_email()

    # get footer (subscribe functionality is contained there)
    footer = main_page.get_footer()

    # method to fill out subscribe field and verify functionality
    footer.subscribe_to_newsletter(email)


def test_subscription_home_page_negative(setup):
    main_page = MainPage(setup)

    # get footer (subscribe functionality is contained there)
    footer = main_page.get_footer()

    # method to fill out subscribe field and verify functionality
    footer.subscribe_to_newsletter("bla")


def test_subscription_cart_positive(setup):
    # classes
    main_page = MainPage(setup)
    cart_page = CartPage(setup)

    # components
    header = main_page.get_header()
    footer = cart_page.get_footer()

    header.click_cart()

    email = get_random_email()
    footer.subscribe_to_newsletter(email)


def test_subscription_cart_negative(setup):
    # classes
    main_page = MainPage(setup)
    cart_page = CartPage(setup)

    # components
    header = main_page.get_header()
    footer = cart_page.get_footer()

    header.click_cart()

    footer.subscribe_to_newsletter("bla")

