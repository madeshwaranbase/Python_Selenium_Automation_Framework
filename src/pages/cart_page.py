from selenium.webdriver.common.by import By
from src.core.base_page import BasePage

class CartPage(BasePage):
    CART_ROWS = (By.CSS_SELECTOR, ".cart-items .cart-item")
    PRODUCT_NAMES = (By.CSS_SELECTOR, ".product-name")
    PROCEED_BUTTON = (By.XPATH, "//button[contains(., 'PROCEED TO CHECKOUT')]")
    PROMO_INPUT = (By.CSS_SELECTOR, "input.promoCode")
    PROMO_BUTTON = (By.CSS_SELECTOR, "button.promoBtn")
    PLACE_ORDER = (By.XPATH, "//button[contains(., 'Place Order')]")

    def product_names(self):
        rows = self.wait.until(lambda d: d.find_elements(*self.CART_ROWS))
        names = []
        for row in rows:
            found = row.find_elements(*self.PRODUCT_NAMES)
            if found:
                names.append(found[0].text.strip())
        return names

    def proceed_to_checkout(self):
        self.click(self.PROCEED_BUTTON)

    def apply_promo_code(self, code: str):
        self.type_text(self.PROMO_INPUT, code)
        self.click(self.PROMO_BUTTON)
