from playwright.sync_api import Page

class ProductPage():
    def __init__(self, page: Page):

        self.product_name = page.locator(".product-information > h2")
        self.product_category = page.locator(".product-information > p").filter(has_text="Category")
        self.product_price = page.locator(".product-information > span > span").filter(has_text="Rs.")
        self.product_availability = page.locator(".product-information > p").filter(has_text="Availability")
        self.product_condition = page.locator(".product-information > p").filter(has_text="Condition")
        self.product_brand = page.locator(".product-information > p").filter(has_text="Brand")

    def get_product_name(self):
        return self.product_name.inner_text()

    def get_product_category(self):
        return self.product_category.inner_text()

    def get_product_price(self):
        return self.product_price.inner_text()

    def get_product_availability(self):
        return self.product_availability.inner_text()

    def get_product_condition(self):
        return self.product_condition.inner_text()

    def get_product_brand(self):
        return self.product_brand.inner_text()





