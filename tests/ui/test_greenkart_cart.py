import pytest
from src.config.settings import settings
from src.pages.home_page import HomePage
from src.pages.cart_page import CartPage

@pytest.mark.ui
def test_search_returns_matching_product(driver):
    home = HomePage(driver, settings.wait_timeout).open(settings.base_url)
    home.search_product("cucumber")
    names = home.product_names()

    assert names, "Search should return at least one product"
    assert all("cucumber" in name.lower() for name in names)

@pytest.mark.ui
def test_add_product_and_verify_cart(driver):
    home = HomePage(driver, settings.wait_timeout).open(settings.base_url)
    home.search_product("cucumber")
    home.add_product("Cucumber")
    home.open_cart()

    cart = CartPage(driver, settings.wait_timeout)
    assert any("cucumber" in name.lower() for name in cart.product_names())
