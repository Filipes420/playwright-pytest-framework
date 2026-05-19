from playwright.sync_api import Page, expect
from components.cart_modal import CartModalComponent

class ProductPage():
    def __init__(self, page: Page):

        self.page = page
        self.product_name = page.locator(".product-information > h2")
        self.product_image = page.locator(".product-details .view-product img")
        self.product_category = page.locator(".product-information > p").filter(has_text="Category")
        self.product_price = page.locator(".product-information > span > span").filter(has_text="Rs.")
        self.product_availability = page.locator(".product-information > p").filter(has_text="Availability")
        self.product_condition = page.locator(".product-information > p").filter(has_text="Condition")
        self.product_brand = page.locator(".product-information > p").filter(has_text="Brand")
        self.product_quantity = page.locator(".product-information #quantity")
        self.add_to_cart_button = page.locator(".product-information button")
        self.cart_modal = page.locator("#cartModal .modal-content")

    def get_product_name(self):
        return self.product_name.inner_text()

    def is_image_loaded(self):
        img = self.product_image
        self.page.wait_for_timeout(1000)
        img.wait_for(state="visible")

        natural_width = img.evaluate("img => img.naturalWidth")

        if natural_width > 0:
            return True

        return False

    def get_product_category(self):
        category_data = self.product_category.inner_text().split(">")
        return category_data[1].strip().lower()

    def get_product_price(self):
        return self.product_price.inner_text().replace("Rs. ", "").strip()

    def get_product_availability(self):
        return self.product_availability.inner_text()

    def get_product_condition(self):
        return self.product_condition.inner_text()

    def get_product_brand(self):
        brand_data = self.product_brand.inner_text().split(":")
        return brand_data[1].strip().upper()

    def set_product_quantity(self, quantity):
        self.product_quantity.fill(quantity)

    def click_add_to_cart_button(self):
        self.add_to_cart_button.click()

    def get_cart_modal(self, go_to_cart=False):
        return CartModalComponent(self.cart_modal)







