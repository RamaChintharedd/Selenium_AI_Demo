from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import shutil
from project.config.config import config


class DriverFactory:
    """Factory to create WebDriver instances based on configuration.

    Keeps construction logic isolated (Single Responsibility) and easily extensible.
    """

    @staticmethod
    def create_driver():
        browser = config.BROWSER
        if browser == "chrome":
            return DriverFactory._create_chrome()
        elif browser == "firefox":
            return DriverFactory._create_firefox()
        else:
            raise ValueError(f"Unsupported browser: {browser}")

    @staticmethod
    def _create_chrome():
        chrome_path = shutil.which("chromedriver")
        if not chrome_path:
            raise EnvironmentError("chromedriver not found in PATH")
        options = ChromeOptions()
        options.add_argument("--start-maximized")
        # options.add_argument('--headless')  # enable for CI if needed
        service = ChromeService()
        driver = webdriver.Chrome(service=service, options=options)
        return driver

    @staticmethod
    def _create_firefox():
        gecko_path = shutil.which("geckodriver")
        if not gecko_path:
            raise EnvironmentError("geckodriver not found in PATH")
        options = FirefoxOptions()
        options.add_argument("--width=1280")
        options.add_argument("--height=800")
        service = FirefoxService()
        driver = webdriver.Firefox(service=service, options=options)
        return driver
