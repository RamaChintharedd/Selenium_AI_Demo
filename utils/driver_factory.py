from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from typing import Optional
from .config import Config


class DriverFactory:
    """Factory to create WebDriver instances. Single Responsibility: driver creation only."""

    @staticmethod
    def create_driver(headless: Optional[bool] = None):
        headless = Config.HEADLESS if headless is None else headless
        browser = Config.BROWSER.lower()

        if browser == "chrome":
            options = ChromeOptions()
            if headless:
                options.add_argument("--headless=new")
                options.add_argument("--window-size=1920,1080")
            options.add_argument("--disable-gpu")
            options.add_argument("--no-sandbox")
            service = ChromeService(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service, options=options)
        elif browser == "firefox":
            options = FirefoxOptions()
            if headless:
                options.add_argument("-headless")
            service = FirefoxService(GeckoDriverManager().install())
            driver = webdriver.Firefox(service=service, options=options)
        else:
            raise ValueError(f"Unsupported browser: {browser}")

        driver.implicitly_wait(Config.IMPLICIT_WAIT)
        driver.maximize_window()
        return driver


__all__ = ["DriverFactory"]
