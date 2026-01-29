from playwright.sync_api import Page, expect

class CheckOutPage():
    def __init__(self, page: Page):
        self.delivery_information = page.locator("#address_delivery li")
        self.cart_header = page.locator("thead > tr")
        self.cart_table_products = page.locator("tbody > tr")
        self.place_order_button = page.locator("a").filter(has_text="Place Order")

    def verify_delivery_information(self):
        expected = ["Your delivery address",
                    "Mr. Filip Gonda",
                    "",
                    "Vojkovce",
                    "30",
                    "Vojkovce Slovenská republika 05361",
                    "United States",
                    "0950461967"]

        expect(self.delivery_information).to_have_count(len(expected))

        for i, value in enumerate(expected):
            expect(self.delivery_information.nth(i)).to_have_text(value)

    def verify_cart_header(self):
        labels = ["Item", "Description", "Price", "Quantity", "Total", ""]

        expect(self.cart_header.locator("td")).to_have_count(len(labels))

        for i in range(self.cart_header.count()):
            header_label = self.cart_header.locator("td").nth(i).inner_text().strip()
            assert header_label in labels

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

    def verify_cart(self, products: list):
        self.verify_cart_header()
        self.verify_cart_products(products)

    def click_place_order_button(self):
        self.place_order_button.click()



