import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def create_driver(browser: str = None):
    """Factory to create and configure WebDriver instances.

    Uses environment variables to control headless mode and browser selection.
    """
    browser = browser or os.getenv('BROWSER', 'chrome').lower()
    headless = os.getenv('HEADLESS', 'true').lower() in ('1', 'true', 'yes')

    if browser == 'firefox':
        opts = FirefoxOptions()
        if headless:
            opts.add_argument('--headless')
        driver = webdriver.Firefox(options=opts)
    else:
        opts = Options()
        # Recommended options for stability in CI
        opts.add_argument('--no-sandbox')
        opts.add_argument('--disable-dev-shm-usage')
        if headless:
            opts.add_argument('--headless=new')
        # Allow overriding Chrome binary path
        chrome_path = os.getenv('CHROME_BINARY')
        if chrome_path:
            opts.binary_location = chrome_path
        driver = webdriver.Chrome(options=opts)

    driver.maximize_window()
    return driver
