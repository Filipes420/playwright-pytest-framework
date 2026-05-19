
class CartModalComponent():
    def __init__(self, root_locator):
        self.root = root_locator

    def get_header(self):
        return self.root.locator("h4").inner_text().strip()

    def get_body(self):
        return self.root.locator("p", has_text="Your product has been added to cart.").inner_text().strip()

    def click_view_cart(self):
        self.root.locator("a").click()

    def click_continue(self):
        self.root.locator("button").click()
