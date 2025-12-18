from itertools import count

from playwright.sync_api import Page, expect

class CartPage():
    def __init__(self, page: Page):
        self.subscribe_email_field = page.locator("#susbscribe_email")
        self.subscribe_button = page.locator("#subscribe")
        self.subscribe_message = page.locator("#success-subscribe")
        self.success_message_div = page.locator(".alert-success")
        self.cart_button = page.get_by_role("link", name=" Cart")
        self.cart_table_header = page.locator("thead > tr")
        self.cart_table_products = page.locator("tbody > tr")
        self.home_button = page.get_by_role("link", name=" Home")

    def subscribe_to_newsletter(self, email):
        self.subscribe_email_field.fill(email)
        self.subscribe_button.click()
        if email == "random" or email is None:

            expect(self.subscribe_message).to_have_class("col-md-9 hide form-group")
            expect(self.success_message_div).not_to_be_visible()

        else:
            expect(self.subscribe_message).to_have_class("col-md-9 form-group")
            expect(self.success_message_div).to_be_visible()

    def get_cart_column_count(self):
        return self.cart_table_header.locator("td").count()

    def verify_cart_header(self):
        labels = ["Item", "Description", "Price", "Quantity", "Total", ""]
        column_count = self.get_cart_column_count()
        assert column_count == 6

        print(column_count)

        for i in range(column_count):
            header_column_label = self.cart_table_header.locator("td").nth(i).inner_text().strip()
            assert header_column_label in labels

    def verify_cart_products(self, products: list):
        expected_products = {}

        for p in products:
            key = p["name"]
            value = p
            expected_products[key] = value


        for i in range(self.cart_table_products.count()):
            product = self.cart_table_products.nth(i)

            product_name = product.locator(".cart_description a").inner_text().strip()
            product_price = product.locator(".cart_price p").inner_text().strip()
            product_quantity = product.locator(".cart_quantity button").inner_text().strip()

            expected_product = expected_products[product_name]

            assert None != expected_product
            assert product_price == expected_product["price"]
            assert product_quantity == expected_product["quantity"]

    def delete_all_cart_products(self):
        cart_products_count = self.cart_table_products.count()

        if cart_products_count > 0:
            for i in range(self.cart_table_products.count()):
                product = self.cart_table_products.nth(i)

                product.locator(".cart_delete a").click()

    #wrapper
    def verify_cart(self, products: list):
        self.verify_cart_header()
        self.verify_cart_products(products)

    def click_home_button(self):
        self.home_button.click()





