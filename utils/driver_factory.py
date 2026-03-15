import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def create_chrome_driver(headless: bool = False, implicit_wait: int = 0):
    """Create and return a Chrome WebDriver using webdriver-manager.
    Headless mode can be enabled via parameter.
    """
    options = Options()
    if headless:
        options.add_argument("--headless=new")
        options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--window-size=1920,1080")
    # Add additional options as needed

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    if implicit_wait:
        driver.implicitly_wait(implicit_wait)

    return driver
