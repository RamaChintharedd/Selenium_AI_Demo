from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from typing import Tuple


class BasePage:
    """
    BasePage contains common utilities used by all Page Objects.
    Keeps page-specific classes focused on their own responsibilities.
    """

    def __init__(self, driver: WebDriver, timeout: int = 10) -> None:
        self.driver = driver
        self.timeout = timeout

    def _wait_for_element_visible(self, locator: Tuple[str, str]):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def _wait_for_element_clickable(self, locator: Tuple[str, str]):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def click(self, locator: Tuple[str, str]) -> None:
        element = self._wait_for_element_clickable(locator)
        element.click()

    def enter_text(self, locator: Tuple[str, str], text: str) -> None:
        element = self._wait_for_element_visible(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator: Tuple[str, str]) -> str:
        element = self._wait_for_element_visible(locator)
        return element.text

    def is_element_present(self, locator: Tuple[str, str]) -> bool:
        try:
            self._wait_for_element_visible(locator)
            return True
        except Exception:
            return False

    def navigate_to(self, url: str) -> None:
        self.driver.get(url)
