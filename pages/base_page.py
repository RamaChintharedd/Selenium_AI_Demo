from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:
    """
    BasePage encapsulates common Selenium WebDriver actions and waits.
    All page objects should inherit from this class.
    """

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout
        self.wait = WebDriverWait(self.driver, self.timeout)

    def visit(self, url):
        """Navigate to a URL."""
        self.driver.get(url)

    def find(self, by, locator):
        """Find a single element after waiting for its presence."""
        return self.wait.until(EC.presence_of_element_located((by, locator)))

    def find_visible(self, by, locator):
        """Wait until the element is visible and return it."""
        return self.wait.until(EC.visibility_of_element_located((by, locator)))

    def click(self, by, locator):
        """Click an element after ensuring it is clickable."""
        el = self.wait.until(EC.element_to_be_clickable((by, locator)))
        el.click()

    def type(self, by, locator, text, clear_first=True):
        """Type text into an input field."""
        el = self.find_visible(by, locator)
        if clear_first:
            el.clear()
        el.send_keys(text)

    def get_text(self, by, locator):
        el = self.find_visible(by, locator)
        return el.text

    def is_element_present(self, by, locator, visible=False):
        """Check presence (or visibility) of element. Returns boolean."""
        try:
            if visible:
                self.find_visible(by, locator)
            else:
                self.find(by, locator)
            return True
        except TimeoutException:
            return False

    def current_url(self):
        return self.driver.current_url

    def wait_for_url(self, expected_url):
        """Wait until the current URL is the expected_url."""
        try:
            return self.wait.until(EC.url_to_be(expected_url))
        except TimeoutException:
            return False
