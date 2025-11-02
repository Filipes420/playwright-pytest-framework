import pytest
from pages.main_page import MainPage
from pages.signin_register_page import SignInRegisterPage
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="function")
def setup():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    playwright.selectors.set_test_id_attribute("data-qa")


    main_page = MainPage(page)
    main_page.start()
    main_page.click_login()

    login_page = SignInRegisterPage(page)

    assert login_page.verify_login_header() == "Login to your account"

    login_page.enter_mail("filip.gonda1@gmail.com")
    login_page.enter_password("Test123")
    login_page.click_login_button()

    page.pause()

    yield page
    browser.close()
    playwright.stop()

