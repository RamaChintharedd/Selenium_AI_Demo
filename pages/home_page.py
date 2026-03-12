from selenium.webdriver.common.by import By
from .base_page import BasePage


class HomePage(BasePage):
    """
    Page object for the demo web shop homepage.
    Encapsulates locators and interactions on the home page.
    """

    LOGIN_LINK = (By.LINK_TEXT, "Log in")

    def __init__(self, driver, base_url="https://demowebshop.tricentis.com"):
        super().__init__(driver)
        self.base_url = base_url

    def load(self):
        """Navigate to the homepage."""
        self.driver.get(self.base_url)

    def click_login(self):
        """Locate and click the 'Log in' link or button."""
        self.click(*self.LOGIN_LINK)
