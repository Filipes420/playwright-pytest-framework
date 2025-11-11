from conftest import setup
from data.data_generator import contact_form_data
from pages.contact_us_page import ContactUsPage
from pages.main_page import MainPage

def test_contact_us_form(setup):

    ## vytvaram triedu main page
    main_page = MainPage(setup)
    main_page.click_contact_us()

    ## vytvaram triedu contact us page
    contact_us_page = ContactUsPage(setup)

    assert contact_us_page.get_in_touch_heading() == "GET IN TOUCH"

    #generate data to fill, fill form and submit
    data_to_fill = contact_form_data()
    contact_us_page.fill_contact_form(data_to_fill["name"], data_to_fill["email"], data_to_fill["subject"],data_to_fill["message"])
    contact_us_page.submit_form()



