import re
import pytest
from playwright.sync_api import Page, expect

@pytest.mark.login
def test_login_positive(setup) -> None:
    page = setup

    page.get_by_role("link", name=" Signup / Login").click()
    page.locator("form").filter(has_text="Login").get_by_placeholder("Email Address").click()
    page.locator("form").filter(has_text="Login").get_by_placeholder("Email Address").fill("filip.gonda1@gmail.com")
    page.locator("form").filter(has_text="Login").get_by_placeholder("Email Address").press("Tab")
    page.get_by_role("textbox", name="Password").fill("Test123")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("link", name=" Logout").click()


def test_logout_positive(setup) -> None:
    page = setup

    page.get_by_role("link", name=" Signup / Login").click()
    page.locator("form").filter(has_text="Login").get_by_placeholder("Email Address").click()
    page.locator("form").filter(has_text="Login").get_by_placeholder("Email Address").fill("filip.gonda1@gmail.com")
    page.locator("form").filter(has_text="Login").get_by_placeholder("Email Address").press("Tab")
    page.get_by_role("textbox", name="Password").fill("Test123")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("link", name=" Logout").click()