import playwright
import pytest

@pytest.fixture(scope="function")
def setup(page):

    ## not needed when using page fixture
    ##browser = playwright.chromium.launch(headless=False)
    ##context = browser.new_context()
    ##page = context.new_page()

    page.goto("https://automationexercise.com/")

    yield page

    ##same
    ##context.close()
    ##browser.close()