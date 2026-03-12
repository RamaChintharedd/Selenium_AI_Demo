from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os


def create_chrome_driver(headless: bool = False):
    """
    Create a Chrome WebDriver instance.
    Set HEADLESS environment variable to '1' to run headless by default.
    """
    chrome_options = Options()
    headless_env = os.getenv('HEADLESS', '0')
    if headless or headless_env == '1':
        chrome_options.add_argument('--headless=new')
        chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    # Optional: set window size for consistent layout
    chrome_options.add_argument('--window-size=1920,1080')

    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    return driver
