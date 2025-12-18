from conftest import setup
from pages.main_page import MainPage
from pages.cart_page import CartPage
from data.data_generator import get_random_email

def test_subscription_home_page_positive(setup):
    main_page = MainPage(setup)

    email = get_random_email()
    main_page.subscribe_to_newsletter(email)


def test_subscription_home_page_negative(setup):
    main_page = MainPage(setup)

    main_page.subscribe_to_newsletter("random")


def test_subscription_cart_positive(setup):
    main_page = MainPage(setup)
    cart_page = CartPage(setup)

    main_page.click_cart()

    email = get_random_email()
    cart_page.subscribe_to_newsletter(email)


def test_subscription_cart_negative(setup):
    main_page = MainPage(setup)
    cart_page = CartPage(setup)

    main_page.click_cart()

    cart_page.subscribe_to_newsletter("random")

