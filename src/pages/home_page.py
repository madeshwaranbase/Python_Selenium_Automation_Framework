from selenium.webdriver.common.by import By
from src.core.base_page import BasePage

class HomePage(BasePage):
    SEARCH = (By.CSS_SELECTOR, "input.search-keyword")
    PRODUCT_CARDS = (By.CSS_SELECTOR, ".products .product")
    CART_ICON = (By.CSS_SELECTOR, "a.cart-icon")
    CART_BADGE = (By.CSS_SELECTOR, ".cart-count")
    PRODUCT_NAME = (By.CSS_SELECTOR, "h4.product-name")
    ADD_BUTTON = (By.XPATH, ".//button[contains(., 'ADD TO CART')]")

    def open(self, url: str):
        self.driver.get(url)
        self.visible(self.SEARCH)
        return self

    def search_product(self, keyword: str):
        self.type_text(self.SEARCH, keyword)
        return self

    def product_names(self):
        cards = self.wait.until(
            lambda d: d.find_elements(*self.PRODUCT_CARDS)
        )
        return [
            card.find_element(*self.PRODUCT_NAME).text.split(" - ")[0].strip()
            for card in cards
        ]

    def add_product(self, product_name: str):
        cards = self.wait.until(lambda d: d.find_elements(*self.PRODUCT_CARDS))
        for card in cards:
            name = card.find_element(*self.PRODUCT_NAME).text
            if product_name.lower() in name.lower():
                card.find_element(*self.ADD_BUTTON).click()
                return
        raise AssertionError(f"Product not found: {product_name}")

    def open_cart(self):
        self.click(self.CART_ICON)
