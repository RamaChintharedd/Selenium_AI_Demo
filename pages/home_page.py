from selenium.webdriver.common.by import By
from .base_page import BasePage


class HomePage(BasePage):
    """Page object for the Demo Web Shop homepage.
    Provides actions relevant to navigation from the homepage.
    """

    # Locators
    LOGIN_LINK = (By.LINK_TEXT, "Log in")

    def __init__(self, driver):
        super().__init__(driver)

    def open(self, base_url: str) -> None:
        """Navigate to the homepage URL."""
        self.driver.get(base_url)

    def go_to_login(self) -> None:
        """Click the login link/button to navigate to the login page."""
        self.click(*self.LOGIN_LINK)
