from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from typing import Tuple, Optional


class BasePage:
    """Base page with common utilities. All pages should inherit from this."""

    def __init__(self, driver: WebDriver, timeout: int = 10):
        self.driver = driver
        self.timeout = timeout

    def go_to(self, url: str):
        """Navigate the browser to a URL."""
        self.driver.get(url)

    def find(self, by: By, locator: str):
        """Find element using explicit wait until visible."""
        wait = WebDriverWait(self.driver, self.timeout)
        return wait.until(EC.visibility_of_element_located((by, locator)))

    def find_optional(self, by: By, locator: str, timeout: Optional[int] = None):
        """Find element but return None if not present within timeout."""
        wait = WebDriverWait(self.driver, timeout or self.timeout)
        try:
            return wait.until(EC.visibility_of_element_located((by, locator)))
        except TimeoutException:
            return None

    def click(self, by: By, locator: str):
        el = self.find(by, locator)
        el.click()

    def type(self, by: By, locator: str, text: str):
        el = self.find(by, locator)
        el.clear()
        el.send_keys(text)

    def get_current_url(self) -> str:
        return self.driver.current_url

    def is_element_present(self, by: By, locator: str, timeout: Optional[int] = None) -> bool:
        return self.find_optional(by, locator, timeout) is not None

    def get_text(self, by: By, locator: str) -> str:
        el = self.find(by, locator)
        return el.text
