from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from typing import Tuple, Optional
from utils.wait_utils import WaitUtils


class BasePage:
    """Base page with common operations. Open for extension but closed for modification (SRP + OCP).

    This class provides low-level actions used by specific page objects.
    """

    def __init__(self, driver: WebDriver, base_url: Optional[str] = None):
        self.driver = driver
        self.wait = WaitUtils(driver)
        self.base_url = base_url

    def open(self, path: str = "") -> None:
        url = path if path.startswith("http") else (self.base_url or "") + path
        self.driver.get(url)

    def _find(self, locator: Tuple) -> object:
        return self.wait.until_visible(locator)

    def click(self, locator: Tuple) -> None:
        element = self.wait.until_clickable(locator)
        element.click()

    def type(self, locator: Tuple, text: str) -> None:
        el = self._find(locator)
        el.clear()
        el.send_keys(text)

    def get_text(self, locator: Tuple) -> str:
        el = self._find(locator)
        return el.text

    def is_displayed(self, locator: Tuple) -> bool:
        try:
            el = self._find(locator)
            return el.is_displayed()
        except AssertionError:
            return False


__all__ = ["BasePage"]
