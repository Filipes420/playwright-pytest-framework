from playwright.sync_api import Page
from utils.text_utils import clean_text
import csv

class ProductsPage():
    def __init__(self, page: Page):
        self.page = page
        self.all_products_heading = page.get_by_role("heading", name="All Products")
        self.products = page.locator(".features_items .productinfo")
        self.view_product_button = page.locator(".features_items .choose li > a").first
        self.search_product_field = page.locator("#advertisement #search_product")
        self.search_button = page.locator("#advertisement #submit_search")
        self.searched_products_header = page.locator(".features_items > h2")

    def get_products_header(self):
        return self.all_products_heading.inner_text()

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







