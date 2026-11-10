from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, timeout: int = 10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def click(self, locator):
        self.clickable(locator).click()

    def type_text(self, locator, value: str, clear: bool = True):
        element = self.visible(locator)
        if clear:
            element.clear()
        element.send_keys(value)
        return element

    def text_of(self, locator) -> str:
        return self.visible(locator).text.strip()
