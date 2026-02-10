from playwright.sync_api import Page, expect
from data.data_generator import create_card_information
from pages.base_page import BasePage

class PaymentPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.name_on_card_field = page.get_by_test_id("name-on-card")
        self.card_number_field = page.get_by_test_id("card-number")
        self.cvc_field = page.get_by_test_id("cvc")
        self.expiry_month_field = page.get_by_test_id("expiry-month")
        self.expiry_year_field = page.get_by_test_id("expiry-year")
        self.pay_and_confirm_order_button = page.get_by_test_id("pay-button")
        self.order_placed_div = page.get_by_test_id("order-placed")
        self.continue_button = page.get_by_test_id("continue-button")
        self.download_invoice_button = page.get_by_role("link", name="Download Invoice")



    def fill_out_card_details_form(self):
        card_details = create_card_information()
        self.name_on_card_field.fill("Filip Gonda")
        self.card_number_field.fill(card_details["card_number"])
        self.cvc_field.fill(card_details["cvv"])

        expiry_numbers = card_details["expiry_date"].split("/")

        self.expiry_month_field.fill(expiry_numbers[0])
        self.expiry_year_field.fill(expiry_numbers[1])

    def submit_order(self):
        self.pay_and_confirm_order_button.click()
        expect(self.order_placed_div).to_have_text("Order Placed!")

    def download_order_invoice(self):
        self.download_file(trigger_action=lambda: self.download_invoice_button.click())


