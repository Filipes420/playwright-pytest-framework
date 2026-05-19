from playwright.sync_api import Page, expect
from components.header import HeaderComponent
from components.left_sidebar import LeftSidebarComponent
from components.footer import FooterComponent


class MainPage:

    def __init__(self, page: Page):
        self.page = page
        self.footer = page.locator("#footer")
        self.header = page.locator("#header")
        self.left_sidebar = page.locator(".left-sidebar")

    def start(self):
        self.page.goto("https://automationexercise.com/")

    def get_header(self):
        return HeaderComponent(self.header)

    def get_left_sidebar(self):
        return LeftSidebarComponent(self.left_sidebar)

    def get_footer(self):
        return FooterComponent(self.footer)



