class HeaderComponent:
    def __init__(self, root_locator):
        self.root = root_locator
        self.home = self.root.get_by_role("link", name="Home")
        self.products = self.root.get_by_role("link", name="Products")
        self.cart = self.root.get_by_role("link", name="Cart")
        self.logout = self.root.get_by_role("link", name="Logout")
        self.delete_account = self.root.get_by_role("link", name="Delete Account")
        self.login = self.root.get_by_role("link", name="Login")
        self.contact_us = self.root.get_by_role("link", name="Contact us")

    def click_home(self):
        self.home.click()

    def click_products(self):
        self.products.click()

    def click_cart(self):
        self.cart.click()

    def click_logout(self):
        self.logout.click()

    def click_delete_account(self):
        self.delete_account.click()

    def click_login(self):
        self.login.click()

    def click_contact_us(self):
        self.contact_us.click()