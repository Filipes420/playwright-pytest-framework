from playwright.sync_api import Page

class MainPage:
    def __init__(self, page: Page):
        self.page = page

    def start(self):
        self.page.goto("https://automationexercise.com/")

    def click_login(self):
        self.page.get_by_role("link", name=" Signup / Login").click()