from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def create_driver(browser: str = "chrome", headless: bool = False):
    """
    Create and return a WebDriver instance.
    Defaults to Chrome via webdriver-manager. Pass headless=True to run headless.
    """
    browser = (browser or "chrome").lower()

    if browser == "chrome":
        options = webdriver.ChromeOptions()
        if headless:
            options.add_argument("--headless=new")
            options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920,1080")
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        if headless:
            options.headless = True
        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service, options=options)
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.implicitly_wait(2)
    return driver
