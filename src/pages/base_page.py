from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:
    """Base page containing common utilities for all page objects."""

    def __init__(self, driver, timeout: int = 15):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self, url: str):
        self.driver.get(url)

    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def finds(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def click(self, locator):
        elm = self.wait.until(EC.element_to_be_clickable(locator))
        elm.click()
        return elm

    def type(self, locator, text: str, clear_first: bool = True):
        elm = self.find(locator)
        if clear_first:
            elm.clear()
        elm.send_keys(text)
        return elm

    def wait_for_text(self, locator, text: str):
        return self.wait.until(EC.text_to_be_present_in_element(locator, text))

    def is_visible(self, locator) -> bool:
        try:
            return EC.visibility_of_element_located(locator)(self.driver)
        except TimeoutException:
            return False
