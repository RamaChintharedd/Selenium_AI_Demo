from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from project.config.config import config


class WaitUtils:
    @staticmethod
    def wait_for_element(driver, locator, timeout=None):
        timeout = timeout or config.DEFAULT_TIMEOUT
        try:
            return WebDriverWait(driver, timeout).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            return None

    @staticmethod
    def wait_for_clickable(driver, locator, timeout=None):
        timeout = timeout or config.DEFAULT_TIMEOUT
        try:
            return WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(locator))
        except TimeoutException:
            return None
