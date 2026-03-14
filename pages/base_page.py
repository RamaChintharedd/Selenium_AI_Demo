from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver
from utils import config

# BasePage implements common utilities used by all page objects. Single Responsibility Principle: one class for common page behavior.
class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, config.EXPLICIT_WAIT)

    def open(self, url: str):
        self.driver.get(url)

    def find(self, by_locator):
        return self.wait.until(EC.presence_of_element_located(by_locator))

    def find_visible(self, by_locator):
        return self.wait.until(EC.visibility_of_element_located(by_locator))

    def click(self, by_locator):
        element = self.find_visible(by_locator)
        element.click()

    def type(self, by_locator, text: str):
        element = self.find_visible(by_locator)
        element.clear()
        element.send_keys(text)

    def is_element_visible(self, by_locator) -> bool:
        try:
            self.find_visible(by_locator)
            return True
        except TimeoutException:
            return False

    def current_url_contains(self, substring: str) -> bool:
        try:
            return self.wait.until(lambda d: substring in d.current_url)
        except TimeoutException:
            return False
