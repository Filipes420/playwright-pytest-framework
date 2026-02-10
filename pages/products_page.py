from playwright.sync_api import Page, expect
from utils.text_utils import clean_text
from data.data_generator import get_random_product


import csv

class ProductsPage():
    def __init__(self, page: Page):
        self.page = page
        self.products = page.locator(".features_items .productinfo")
        self.view_product_button = page.locator(".features_items .choose li > a").first
        self.search_product_field = page.locator("#advertisement #search_product")
        self.search_button = page.locator("#advertisement #submit_search")
        self.searched_products_header = page.locator(".features_items > h2")
        self.added_to_cart_modal_header = page.locator(".modal-content h4")
        self.added_to_cart_modal_body = page.locator(".modal-content p").filter(has_text="Your product has been added to cart.")
        self.added_to_cart_modal_view_cart = page.locator(".modal-content a")
        self.added_to_cart_modal_continue_button = page.locator(".modal-content button")
        self.cart_button = page.get_by_role("link", name=" Cart")

    def get_products_header(self):
        return self.page.locator(".features_items > h2").inner_text().strip().lower()

    def get_products_count(self):
        return self.products.count()

    def verify_all_products(self):
        count = self.get_products_count()

        ## check every product
        for i in range(count):
            product = self.products.nth(i)

            ## product image check by size
            img = product.locator("img")
            img.wait_for(state="visible", timeout=5000)
            natural_width = img.evaluate("img => img.naturalWidth")
            assert natural_width > 0

            ## price tag visibility check
            price_tag = product.locator("h2")
            price_tag.is_visible()

            ## price number check (>0)
            price_text = price_tag.inner_text()
            price = int(price_text.replace("Rs. ","").strip())
            assert price > 0

            ## product tag visibility check
            product_name_paragraph = product.locator("p")
            assert product_name_paragraph.is_visible()

            ## product name check
            product_name = clean_text(product_name_paragraph.inner_text())
            assert product_name.isalpha() == True

            assert product.locator("a.add-to-cart").is_visible()

    def click_view_product(self):
        self.view_product_button.click()

    def click_cart_button(self):
        self.cart_button.click()

    def search_product(self, product_to_search):
        self.search_product_field.fill(product_to_search)
        self.search_button.click()

    def get_searched_products_header(self):
        return self.searched_products_header.inner_text()

    def verify_searched_products(self, product_name, product_price=None):
        count = self.get_products_count()

        for i in range(count):
            product = self.products.nth(i)

            if product_price:
                assert product_name == product.locator("p").inner_text()
                assert product_price == product.locator("h2").inner_text()

            assert product_name in product.locator("p").inner_text()

    def get_product_names(self):
        product_names = []
        count = self.get_products_count()

        for i in range(count):
            product = self.products.nth(i)
            product_name = product.locator("p").inner_text().strip()
            product_names.append(product_name)

        return product_names

    def add_product_to_cart(self):
        product = self.products
        product.locator("a").click()


    def verify_added_to_cart_popup(self, go_to_cart = False):
        expect(self.added_to_cart_modal_header).to_have_text("Added!")
        expect(self.added_to_cart_modal_body).to_have_text("Your product has been added to cart.")
        expect(self.added_to_cart_modal_view_cart).to_be_visible()
        expect(self.added_to_cart_modal_continue_button).to_be_visible()

        if go_to_cart == True:
            self.added_to_cart_modal_view_cart.click()

        else:
            self.added_to_cart_modal_continue_button.click()

    #wrapper function to add multiple product to cart at once
    def add_multiple_products_to_cart(self, product_count):

        ## list of product names
        products_by_name = {}

        ## iterate based on product_count
        for i in range(product_count):
            product = get_random_product()
            name = product["name"]

            self.search_product(name)
            self.verify_searched_products(name)

            if name in products_by_name:
                products_by_name[name]["quantity"] = str(int(products_by_name[name]["quantity"]) + 1)
            else:
                product["quantity"] = "1"
                products_by_name[name] = product

            self.add_product_to_cart()

            self.verify_added_to_cart_popup(i == product_count - 1)

        return list(products_by_name.values())




    def scrap_product_data(self):

        count = self.get_products_count()
        data = []
        for i in range(count):

            product = self.products.nth(i)
            name = product.locator("p").inner_text()
            price = product.locator("h2").inner_text()
            data.append([name, price])

        with open("data/products_data.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["name", "price"])
            writer.writerows(data)







