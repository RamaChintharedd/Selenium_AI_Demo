from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
import os


def create_chrome_driver(headless=False, implicit_wait=5):
    """
    Create and configure a Chrome WebDriver instance.
    Extracted to factory for single responsibility and test scalability.
    """
    options = Options()
    if headless:
        options.add_argument("--headless=new")
        options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    # Allow overriding chrome binary & webdriver path via env vars if desired
    chrome_binary = os.environ.get("CHROME_BINARY")
    if chrome_binary:
        options.binary_location = chrome_binary

    webdriver_path = os.environ.get("CHROMEDRIVER_PATH")
    if webdriver_path:
        service = ChromeService(executable_path=webdriver_path)
        driver = webdriver.Chrome(service=service, options=options)
    else:
        # Assume chromedriver is on PATH
        driver = webdriver.Chrome(options=options)

    driver.implicitly_wait(implicit_wait)
    driver.maximize_window()
    return driver
