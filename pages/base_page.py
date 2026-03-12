from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from utils.wait_utils import wait_for_element, wait_for_clickable
from config import DEFAULT_TIMEOUT


class BasePage:
    """
    BasePage encapsulates common behaviors for all pages.
    """
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open_url(self, url: str):
        self.driver.get(url)

    def find(self, locator, timeout=DEFAULT_TIMEOUT):
        return wait_for_element(self.driver, locator, timeout)

    def click(self, locator, timeout=DEFAULT_TIMEOUT):
        elem = wait_for_clickable(self.driver, locator, timeout)
        if elem:
            elem.click()
            return True
        return False

    def get_current_url(self) -> str:
        return self.driver.current_url

    def get_text(self, locator, timeout=DEFAULT_TIMEOUT) -> str:
        el = self.find(locator, timeout)
        return el.text.strip() if el else ""
