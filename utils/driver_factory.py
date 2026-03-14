from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service as FFService
from selenium.webdriver.firefox.options import Options as FFOptions
import shutil
import os

# Minimal driver factory supporting Chrome and Firefox. Extendable for cloud providers.
class DriverFactory:
    @staticmethod
    def create_chrome_driver(headless: bool = True):
        chrome_opts = Options()
        if headless:
            chrome_opts.add_argument("--headless=new")
        chrome_opts.add_argument("--window-size=1920,1080")
        chrome_opts.add_argument("--no-sandbox")
        chrome_opts.add_argument("--disable-dev-shm-usage")

        # Attempt to locate chromedriver in PATH
        chromedriver_path = shutil.which("chromedriver")
        if chromedriver_path:
            service = Service(chromedriver_path)
            driver = webdriver.Chrome(service=service, options=chrome_opts)
        else:
            # If running in environment with bundled browser, webdriver-manager or other tooling should be used.
            driver = webdriver.Chrome(options=chrome_opts)
        return driver

    @staticmethod
    def create_firefox_driver(headless: bool = True):
        ff_opts = FFOptions()
        if headless:
            ff_opts.headless = True
        ff_opts.add_argument("--width=1920")
        ff_opts.add_argument("--height=1080")

        geckodriver_path = shutil.which("geckodriver")
        if geckodriver_path:
            service = FFService(geckodriver_path)
            driver = webdriver.Firefox(service=service, options=ff_opts)
        else:
            driver = webdriver.Firefox(options=ff_opts)
        return driver
