from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HomePage(BasePage):
    """
    Page object representing the homepage of Demo Web Shop.
    """
    LOGIN_LINK = (By.LINK_TEXT, 'Log in')

    def __init__(self, driver):
        super().__init__(driver)

    def open(self, base_url: str):
        """Navigate to the homepage."""
        self.open_url(base_url)

    def click_login(self) -> None:
        """Click the 'Log in' link to navigate to the login page."""
        if not self.click(self.LOGIN_LINK):
            raise Exception("Login link not found or not clickable on homepage")
