from selenium.webdriver.common.by import By
from project.utils.wait_utils import WaitUtils


class BasePage:
    """Common page functionality used by all Page Objects."""

    def __init__(self, driver):
        self.driver = driver

    def find(self, locator):
        return WaitUtils.wait_for_element(self.driver, locator)

    def click(self, locator):
        element = WaitUtils.wait_for_clickable(self.driver, locator)
        if element:
            element.click()
            return True
        return False

    def get_text(self, locator):
        el = self.find(locator)
        return el.text.strip() if el is not None else ""

    def is_displayed(self, locator):
        el = self.find(locator)
        return bool(el and el.is_displayed())
