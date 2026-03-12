from selenium.webdriver.common.by import By
from .base_page import BasePage


class HomePage(BasePage):
    """
    Page object for the Demo Web Shop homepage.
    """

    URL = "https://demowebshop.tricentis.com"

    # Locators
    LOGIN_LINK = (By.LINK_TEXT, "Log in")

    def go_to_homepage(self):
        """Open the homepage."""
        self.visit(self.URL)

    def click_login(self):
        """Click the Log in link on the homepage."""
        # Using click helper from BasePage
        self.click(*self.LOGIN_LINK)
