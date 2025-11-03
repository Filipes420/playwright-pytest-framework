import pytest

from conftest import setup
from pages.main_page import MainPage


def test_logout(setup):
    # musim vytvoriť page z mojej fixture aby som to vedel dať ako argument pri vytvoreni objektu
    page = setup

    # vytvaram objekt main page
    main_page = MainPage(page)

    # klikni logout
    main_page.click_logout()
