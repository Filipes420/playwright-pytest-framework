from playwright.sync_api import Page

class MainPage:
    def __init__(self, page: Page):
        self.page = page
        self.login_button = page.get_by_role("link", name=" Signup / Login")
        self.logout_button = page.get_by_text("Logout")
        self.contact_us_button = page.get_by_role("link", name="Contact us")
        self.products_button = page.get_by_role("link", name="Products")

    def start(self):
        self.page.goto("https://automationexercise.com/")

    def click_login(self):
        self.login_button.click()

    def click_logout(self):
        self.logout_button.click()

    def click_contact_us(self):
        self.contact_us_button.click()

    def click_products(self):
        self.products_button.click()