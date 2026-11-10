from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.safari.options import Options as SafariOptions

from src.config.settings import settings

def create_driver():
    browser = settings.browser

    if browser == "chrome":
        options = ChromeOptions()
        if settings.headless:
            options.add_argument("--headless=new")
        options.add_argument("--window-size=1440,1000")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--no-sandbox")
        return webdriver.Chrome(options=options)

    if browser == "firefox":
        options = FirefoxOptions()
        if settings.headless:
            options.add_argument("-headless")
        return webdriver.Firefox(options=options)

    if browser == "safari":
        return webdriver.Safari(options=SafariOptions())

    raise ValueError(f"Unsupported browser: {browser}")
