

from conftest import setup
from pages.main_page import MainPage


def test_logout(setup):

    # vytvaram objekt main page
    main_page = MainPage(setup)

    # klikni logout

    main_page.click_logout()
