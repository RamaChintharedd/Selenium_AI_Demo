from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from typing import Tuple


class BasePage:
    """BasePage encapsulates common WebDriver actions and waiting utilities.
    Follows Single Responsibility: only provides driver and common helpers.
    """

    def __init__(self, driver: WebDriver, timeout: int = 10) -> None:
        self.driver = driver
        self.timeout = timeout

    def find(self, by: By, locator: str):
        """Find a single element after waiting for presence."""
        return WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located((by, locator))
        )

    def find_visible(self, by: By, locator: str):
        """Wait until an element is visible and return it."""
        return WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located((by, locator))
        )

    def click(self, by: By, locator: str) -> None:
        el = self.find_visible(by, locator)
        el.click()

    def type_text(self, by: By, locator: str, text: str) -> None:
        el = self.find_visible(by, locator)
        el.clear()
        el.send_keys(text)

    def is_displayed(self, by: By, locator: str) -> bool:
        try:
            return self.find_visible(by, locator).is_displayed()
        except TimeoutException:
            return False

    def get_current_url(self) -> str:
        return self.driver.current_url

    def wait_for_url_contains(self, fragment: str) -> bool:
        try:
            WebDriverWait(self.driver, self.timeout).until(
                EC.url_contains(fragment)
            )
            return True
        except TimeoutException:
            return False

    def get_element_text(self, by: By, locator: str) -> str:
        el = self.find_visible(by, locator)
        return el.text
