import pytest

from pages.main_page import MainPage
from data.expected_data import get_expected_categories, get_expected_brands
from pages.products_page import ProductsPage


def test_categories(setup):

    main_page = MainPage(setup)
    products_page = ProductsPage(setup)

    actual_categories = main_page.get_subcategories_left_sidebar()
    expected_categories = get_expected_categories()

    assert main_page.get_categories_heading() == "CATEGORY"
    for category, subcategories in expected_categories.items():
        assert category in actual_categories

        for subcategory in subcategories:
            assert subcategory in actual_categories[category]
            main_page.click_subcategory(category.capitalize(), subcategory.capitalize())

            products_page_header = products_page.get_products_header().capitalize()
            assert category.capitalize(), subcategory.capitalize() in products_page_header

@pytest.mark.skip
def test_brands(setup):

    main_page = MainPage(setup)
    products_page = ProductsPage(setup)

    actual_brands = main_page.get_brands_left_sidebar()
    expected_brands = get_expected_brands()

    assert main_page.get_brands_heading() == "BRANDS"

    for brand, count in actual_brands.items():
        assert brand in expected_brands
        main_page.click_brand(brand)
        assert brand in products_page.get_products_header().upper()
        assert products_page.get_products_count() == int(count)










