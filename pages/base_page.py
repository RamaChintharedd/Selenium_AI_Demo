from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """
    BasePage provides common utilities for all page objects.
    Follow SOLID: single responsibility for common behaviors.
    """

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout
        self.wait = WebDriverWait(self.driver, self.timeout)

    def find(self, by, locator):
        """Wait for element to be present and return it."""
        return self.wait.until(EC.presence_of_element_located((by, locator)))

    def find_all(self, by, locator):
        """Return list of elements (no waiting for visibility of all)."""
        return self.driver.find_elements(by, locator)

    def click(self, by, locator):
        """Wait until clickable and click."""
        el = self.wait.until(EC.element_to_be_clickable((by, locator)))
        el.click()

    def input_text(self, by, locator, text):
        el = self.find(by, locator)
        el.clear()
        el.send_keys(text)

    def get_current_url(self):
        return self.driver.current_url

    def is_element_visible(self, by, locator):
        try:
            self.wait.until(EC.visibility_of_element_located((by, locator)))
            return True
        except Exception:
            return False

    def get_element_text(self, by, locator):
        try:
            el = self.find(by, locator)
            return el.text
        except Exception:
            return ""
