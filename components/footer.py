import re
from playwright.sync_api import expect

class FooterComponent:
    def __init__(self, root_locator):
        self.root = root_locator
        self.subscribe_email_field = self.root.locator("#susbscribe_email")
        self.subscribe_button = self.root.locator("#subscribe")
        self.subscribe_message = self.root.locator("#success-subscribe")
        self.success_message_div = self.root.locator(".alert-success")


    def subscribe_to_newsletter(self, email):
        pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        is_valid = bool(re.fullmatch(pattern, email))
        self.subscribe_email_field.fill(email)

        self.subscribe_button.click()

        if is_valid is False or email is None:

            expect(self.subscribe_message).to_have_class("col-md-9 hide form-group")
            expect(self.success_message_div).not_to_be_visible()

        else:
            expect(self.subscribe_message).to_have_class("col-md-9 form-group")
            expect(self.success_message_div).to_be_visible()