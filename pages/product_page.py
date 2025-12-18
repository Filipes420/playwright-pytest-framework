from playwright.sync_api import Page, expect

class ProductPage():
    def __init__(self, page: Page):

        self.product_name = page.locator(".product-information > h2")
        self.product_category = page.locator(".product-information > p").filter(has_text="Category")
        self.product_price = page.locator(".product-information > span > span").filter(has_text="Rs.")
        self.product_availability = page.locator(".product-information > p").filter(has_text="Availability")
        self.product_condition = page.locator(".product-information > p").filter(has_text="Condition")
        self.product_brand = page.locator(".product-information > p").filter(has_text="Brand")
        self.product_quantity = page.locator(".product-information #quantity")
        self.add_to_cart_button = page.locator(".product-information button")
        self.added_to_cart_modal_header = page.locator(".modal-content h4")
        self.added_to_cart_modal_body = page.locator(".modal-content p").filter(
            has_text="Your product has been added to cart.")
        self.added_to_cart_modal_view_cart = page.locator(".modal-content a")
        self.added_to_cart_modal_continue_button = page.locator(".modal-content button")
        self.products_button = page.get_by_role("link", name="Products")

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

    def set_product_quantity(self, quantity):
        self.product_quantity.fill(quantity)

    def click_add_to_cart_button(self):
        self.add_to_cart_button.click()

    def click_products(self):
        self.products_button.click()

    def verify_added_to_cart_popup(self, go_to_cart=False):
        expect(self.added_to_cart_modal_header).to_have_text("Added!")
        expect(self.added_to_cart_modal_body).to_have_text("Your product has been added to cart.")
        expect(self.added_to_cart_modal_view_cart).to_be_visible()
        expect(self.added_to_cart_modal_continue_button).to_be_visible()

        if go_to_cart == True:
            self.added_to_cart_modal_view_cart.click()

        else:
            self.added_to_cart_modal_continue_button.click()







