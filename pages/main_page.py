from playwright.sync_api import Page, expect
import re

from data.expected_data import get_expected_brands


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
        self.category_heading = page.locator(".left-sidebar > h2")
        self.categories_divs = page.locator("#accordian > div")
        self.brands_heading = page.locator(".brands_products h2")
        self.brands_list = page.locator(".brands_products li")

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

    def get_categories_heading(self):
        return self.category_heading.inner_text().strip()

    def get_categories_count(self):
        return self.categories_divs.count()

    def get_subcategories_left_sidebar(self):
        categories = {}
        category_list_count = self.get_categories_count()

        for i in range(category_list_count):
            category_div = self.categories_divs.nth(i)
            category_heading = category_div.locator("h4").inner_text().strip().lower()
            subcategory_count = category_div.locator("li").count()

            subcategories = []

            for j in range(subcategory_count):
                subcategory_name = category_div.locator("li").nth(j).inner_text().strip().lower()

                subcategories.append(subcategory_name)

            categories[category_heading] = subcategories

        return categories

    def click_subcategory(self, category: str, subcategory: str):
        self.page.locator(f'a[href="#{category}"]').click()
        self.page.locator(f"#{category} .panel-body a",has_text=subcategory).click()

    def get_brands_heading(self):
        return self.brands_heading.inner_text().strip()

    def get_brands_count(self):
        return self.brands_list.count()

    def get_brands_left_sidebar(self):
        brands = {}
        brands_count = self.get_brands_count()

        for i in range(brands_count):
            brand_info = self.brands_list.nth(i).inner_text().strip().split("\n")
            brand_name = brand_info[1]
            brand_products_count = brand_info[0].replace("(", "").replace(")", "").strip()

            brands[brand_name] = brand_products_count

        return brands

    def click_brand(self, brand: str):
        self.brands_list.filter(has_text=brand).click()
















    #def verify_left_sidebar(self):


