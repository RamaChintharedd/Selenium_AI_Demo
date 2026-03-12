from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from typing import Any
import shutil
import os


def create_driver(browser: str = "chrome", headless: bool = False) -> Any:
    """Factory to create WebDriver instances. Keeps test code decoupled from driver details."""
    browser = browser.lower()

    if browser == "chrome":
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        # Allow user to supply CHROME_DRIVER_PATH env var; otherwise rely on webdriver-manager or PATH
        chrome_path = os.getenv("CHROME_DRIVER_PATH")
        if chrome_path and shutil.which(chrome_path):
            service = ChromeService(executable_path=chrome_path)
            return webdriver.Chrome(service=service, options=options)
        return webdriver.Chrome(options=options)

    if browser == "firefox":
        options = FirefoxOptions()
        if headless:
            options.add_argument("-headless")
        firefox_path = os.getenv("GECKO_DRIVER_PATH")
        if firefox_path and shutil.which(firefox_path):
            service = FirefoxService(executable_path=firefox_path)
            return webdriver.Firefox(service=service, options=options)
        return webdriver.Firefox(options=options)

    raise ValueError(f"Unsupported browser: {browser}")
