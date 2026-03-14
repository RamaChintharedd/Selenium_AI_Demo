from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from typing import Optional
import os
from .config import CHROME_DRIVER_PATH


def create_chrome_driver(headless: bool = False, driver_path: Optional[str] = None):
    """Create and configure a Chrome WebDriver instance."""
    chrome_options = Options()
    if headless:
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    path = driver_path or CHROME_DRIVER_PATH
    if path:
        service = ChromeService(path)
        driver = webdriver.Chrome(service=service, options=chrome_options)
    else:
        # Assumes chromedriver is on PATH
        driver = webdriver.Chrome(options=chrome_options)

    # Recommended defaults, explicit waits used in page objects
    driver.implicitly_wait(0)
    return driver


def create_firefox_driver(headless: bool = False, driver_path: Optional[str] = None):
    firefox_options = FirefoxOptions()
    if headless:
        firefox_options.add_argument("-headless")
    path = driver_path
    if path:
        service = FirefoxService(path)
        driver = webdriver.Firefox(service=service, options=firefox_options)
    else:
        driver = webdriver.Firefox(options=firefox_options)
    driver.implicitly_wait(0)
    return driver
