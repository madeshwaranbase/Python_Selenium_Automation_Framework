import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from src.config.settings import settings
from src.pages.home_page import HomePage

scenarios("green_kart.feature")

@pytest.fixture
def home_page(driver):
    return HomePage(driver, settings.wait_timeout)

@given("the GreenKart home page is open")
def open_home(home_page):
    home_page.open(settings.base_url)

@when(parsers.parse('the shopper searches for "{keyword}"'))
def search(home_page, keyword):
    home_page.search_product(keyword)

@then("matching products should be displayed")
def verify_results(home_page):
    names = home_page.product_names()
    assert names
    assert all("cucumber" in name.lower() for name in names)
