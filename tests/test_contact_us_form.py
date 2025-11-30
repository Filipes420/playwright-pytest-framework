import pytest

from conftest import setup
from data.data_generator import create_contact_form_data
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
    data_to_fill = create_contact_form_data()
    contact_us_page.fill_contact_form(data_to_fill["name"], data_to_fill["email"], data_to_fill["subject"],data_to_fill["message"])
    contact_us_page.submit_form(True)



def test_contact_us_form_with_file(setup):

    ## vytvaram triedu main page
    main_page = MainPage(setup)
    main_page.click_contact_us()

    ## vytvaram triedu contact us page
    contact_us_page = ContactUsPage(setup)

    assert contact_us_page.get_in_touch_heading() == "GET IN TOUCH"

    # generate data to fill, fill form and submit
    data_to_fill = create_contact_form_data()
    contact_us_page.fill_contact_form(data_to_fill["name"], data_to_fill["email"], data_to_fill["subject"],
                                      data_to_fill["message"], "data/contact_form_dummy_file.txt")
    contact_us_page.submit_form(True)

@pytest.mark.skip
def test_contact_us_form_mandatory_fields(setup):
    ## vytvaram triedu main page
    main_page = MainPage(setup)
    main_page.click_contact_us()

    ## vytvaram triedu contact us page
    contact_us_page = ContactUsPage(setup)

    assert contact_us_page.get_in_touch_heading() == "GET IN TOUCH"

    data = create_contact_form_data()

    contact_us_page.enter_name(data["name"])
    contact_us_page.enter_subject(data["subject"])
    contact_us_page.enter_message(data["message"])
    contact_us_page.submit_form(False)

    contact_us_page.validate_tooltip()





