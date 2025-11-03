from playwright.sync_api import Page

class MainPage:
    def __init__(self, page: Page):
        self.page = page
        self.login_button = self.page.get_by_role("link", name=" Signup / Login")
        self.logout_button = page.get_by_text("Logout")

    def start(self):
        self.page.goto("https://automationexercise.com/")

    def click_login(self):
        self.login_button.click()

    def click_logout(self):
        self.logout_button.click()