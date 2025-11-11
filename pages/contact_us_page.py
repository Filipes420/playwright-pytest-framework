from playwright.sync_api import Page

class ContactUsPage:
    def __init__(self, page: Page):
        self.page = page
        self.get_in_touch = page.get_by_role("heading", name="Get In Touch")
        self.name_input = page.get_by_test_id("name")
        self.email_input = page.get_by_test_id("email")
        self.subject_input = page.get_by_test_id("subject")
        self.message_input = page.get_by_test_id("message")
        self.upload_file_button = page.locator("//input[@type='file']")
        self.submit_button  = page.get_by_test_id("submit-button")

## one element methods
    def get_in_touch_heading(self):
        return self.get_in_touch.inner_text()

    def enter_name(self, name):
        self.name_input.fill(name)

    def enter_email(self, email):
        self.email_input.fill(email)

    def enter_subject(self, subject):
        self.subject_input.fill(subject)

    def enter_message(self, message):
        self.message_input.fill(message)

    def upload_file(self, filepath):
        with self.page.expect_file_chooser() as fc:
            self.upload_file_button.click()
            file_chooser = fc.value
            file_chooser.set_files(filepath)

    def submit_form(self):
        self.submit_button.click()


## wrapper methods
    def fill_contact_form(self, name, email, subject, message, filepath=None):
        self.enter_name(name)
        self.enter_email(email)
        self.enter_subject(subject)
        self.enter_message(message)

        ## file upload is optional
        if filepath:
            self.upload_file(filepath)


