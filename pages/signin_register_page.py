from playwright.sync_api import Page

class SignInRegisterPage:
    def __init__(self, page: Page):
        self.page = page
        self.login_header = self.page.get_by_role("heading", name = "Login to your account" )
        self.email_input = self.page.get_by_test_id("login-email")
        self.pw_input = self.page.get_by_test_id("login-password")
        self.login_button = self.page.get_by_test_id("login-button")

    def verify_login_header(self):
        return self.login_header.inner_text()

    def enter_mail(self, email):
        self.email_input.fill(email)

    def enter_password(self, password):
        self.pw_input.fill(password)

    def click_login_button(self):
        self.login_button.click()