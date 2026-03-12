from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By


class BasePage:
    """
    BasePage provides common utilities used by all Page Objects.
    Use composition: each Page Object receives a WebDriver instance.
    """

    def __init__(self, driver, timeout: int = 10):
        self.driver = driver
        self.timeout = timeout

    def find(self, by, locator):
        return self.driver.find_element(by, locator)

    def find_all(self, by, locator):
        return self.driver.find_elements(by, locator)

    def click(self, by, locator):
        elem = self.wait_for_element_to_be_clickable(by, locator)
        elem.click()

    def type(self, by, locator, text: str, clear_first: bool = True):
        elem = self.wait_for_presence(by, locator)
        if clear_first:
            elem.clear()
        elem.send_keys(text)

    def wait_for_presence(self, by, locator):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located((by, locator))
        )

    def wait_for_visibility(self, by, locator):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located((by, locator))
        )

    def wait_for_element_to_be_clickable(self, by, locator):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable((by, locator))
        )

    def is_element_present(self, by, locator) -> bool:
        try:
            self.wait_for_presence(by, locator)
            return True
        except TimeoutException:
            return False

    def open_url(self, url: str):
        self.driver.get(url)
