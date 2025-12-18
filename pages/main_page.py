from playwright.sync_api import Page, expect


class MainPage:
    def __init__(self, page: Page):
        self.page = page
        self.login_button = page.get_by_role("link", name=" Signup / Login")
        self.logout_button = page.get_by_text("Logout")
        self.contact_us_button = page.get_by_role("link", name="Contact us")
        self.products_button = page.get_by_role("link", name="Products")
        self.subscribe_email_field = page.locator("#susbscribe_email")
        self.subscribe_button = page.locator("#subscribe")
        self.subscribe_message = page.locator("#success-subscribe")
        self.success_message_div = page.locator(".alert-success")
        self.cart_button = page.get_by_role("link", name=" Cart")

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

    def click_cart(self):
        self.cart_button.click()

    def subscribe_to_newsletter(self, email):
        self.subscribe_email_field.fill(email)
        self.subscribe_button.click()
        if email == "random" or email is None:

            expect(self.subscribe_message).to_have_class("col-md-9 hide form-group")
            expect(self.success_message_div).not_to_be_visible()

        else:
            expect(self.subscribe_message).to_have_class("col-md-9 form-group")
            expect(self.success_message_div).to_be_visible()

