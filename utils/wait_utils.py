from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webelement import WebElement
from typing import Tuple
from .config import Config


class WaitUtils:
    """Utility wrapper around WebDriverWait for readability and reuse."""

    def __init__(self, driver, timeout: int = None):
        self.driver = driver
        self.timeout = Config.EXPLICIT_WAIT if timeout is None else timeout

    def until_visible(self, locator: Tuple, message: str = "") -> WebElement:
        try:
            return WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(locator))
        except TimeoutException as ex:
            raise AssertionError(f"Element not visible: {locator}. {message}") from ex

    def until_clickable(self, locator: Tuple, message: str = "") -> WebElement:
        try:
            return WebDriverWait(self.driver, self.timeout).until(EC.element_to_be_clickable(locator))
        except TimeoutException as ex:
            raise AssertionError(f"Element not clickable: {locator}. {message}") from ex


__all__ = ["WaitUtils"]
