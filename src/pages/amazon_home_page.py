from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from .base_page import BasePage


class AmazonHomePage(BasePage):
    """Page object for Amazon homepage - minimal selectors used for search flows."""

    SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
    SEARCH_SUBMIT = (By.ID, 'nav-search-submit-button')

    def open_home(self, base_url: str = 'https://www.amazon.com'):
        """Navigate to Amazon home page."""
        self.open(base_url)

    def locate_search_input(self):
        return self.find(self.SEARCH_INPUT)

    def enter_search_keyword(self, keyword: str):
        el = self.locate_search_input()
        el.clear()
        el.send_keys(keyword)

    def submit_search(self):
        # Some pages respond to ENTER better; click as fallback
        try:
            self.find(self.SEARCH_INPUT).send_keys(Keys.ENTER)
        except Exception:
            self.click(self.SEARCH_SUBMIT)
