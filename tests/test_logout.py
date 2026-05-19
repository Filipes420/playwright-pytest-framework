from conftest import setup
from pages.main_page import MainPage


def test_logout(setup):

    # classes
    main_page = MainPage(setup)

    header = main_page.get_header()

    header.click_logout()
