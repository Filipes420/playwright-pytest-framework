class CartComponent():
    def __init__(self, root_locator):
        self.root = root_locator

    def get_cart_column_count(self):
        return self.root.locator("thead td").count()

    def get_cart_header_labels(self):
        labels = []
        column_count = self.get_cart_column_count()

        for i in range(column_count):
            labels.append(self.root.locator("thead td").nth(i).inner_text().strip())

        return labels

    def get_cart_products_count(self):
        return self.root.locator("tbody > tr[id^='product-']").count()

    def get_cart_products(self):
        products = []

        for i in range(self.get_cart_products_count()):
            cart_product = self.root.locator("tbody > tr[id^='product-']").nth(i)

            product = {"name": cart_product.locator(".cart_description a").inner_text().strip(),
                       "price": cart_product.locator(".cart_price p").inner_text().replace("Rs. ", "").strip(),
                       "quantity": cart_product.locator(".cart_quantity button").inner_text().strip()}

            products.append(product)

        return products

    def delete_cart_products(self):
        cart_products_count = self.get_cart_products_count()

        if cart_products_count > 0:
            for i in range(cart_products_count):
                product = self.root.locator("tbody > tr").nth(i)
                product.locator(".cart_delete a").click()