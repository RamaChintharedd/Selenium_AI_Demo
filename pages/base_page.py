from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from typing import Tuple, Optional


class BasePage:
    """
    BasePage provides common utilities for all page objects.
    Follows single responsibility: wraps WebDriver and common wait actions.
    """

    def __init__(self, driver: WebDriver, timeout: int = 10):
        self.driver = driver
        self.timeout = timeout
        self.wait = WebDriverWait(self.driver, self.timeout)

    def open_url(self, url: str) -> None:
        """Navigate browser to the specified URL."""
        self.driver.get(url)

    def find(self, locator: Tuple[By, str]):
        """Finds an element using an explicit wait for presence."""
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_visible(self, locator: Tuple[By, str]):
        """Finds an element waiting for it to be visible."""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click(self, locator: Tuple[By, str]):
        """Waits until element is clickable and clicks it."""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def is_element_visible(self, locator: Tuple[By, str]) -> bool:
        """Return True if element is visible within timeout, else False."""
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def get_text(self, locator: Tuple[By, str]) -> Optional[str]:
        """Get text of an element if present and visible; else None."""
        try:
            el = self.find_visible(locator)
            return el.text
        except TimeoutException:
            return None

    def current_url(self) -> str:
        return self.driver.current_url
