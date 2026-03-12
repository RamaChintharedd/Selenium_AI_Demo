from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


class DriverFactory:
    """
    DriverFactory is a simple factory for creating WebDriver instances.
    Supports Chrome and Firefox. Uses webdriver-manager to auto-download drivers.
    Configure via parameters or environment variables in higher-level code.
    """

    @staticmethod
    def create_driver(browser: str = "chrome", headless: bool = False, implicitly_wait: int = 10):
        browser = (browser or "chrome").lower()

        if browser == "chrome":
            options = ChromeOptions()
            if headless:
                # Use new headless mode flag where supported
                try:
                    options.add_argument("--headless=new")
                except Exception:
                    options.add_argument("--headless")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            service = Service(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service, options=options)
        elif browser == "firefox" or browser == "ff":
            options = FirefoxOptions()
            if headless:
                options.add_argument("-headless")
            service = FirefoxService(GeckoDriverManager().install())
            driver = webdriver.Firefox(service=service, options=options)
        else:
            raise ValueError(f"Unsupported browser: {browser}")

        driver.implicitly_wait(implicitly_wait)
        driver.maximize_window()
        return driver
