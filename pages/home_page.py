from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    # Locators grouped at top for clarity and easy maintenance
    LOGIN_LINK = (By.CLASS_NAME, "ico-login")

    def __init__(self, driver):
        super().__init__(driver)

    def open_homepage(self, base_url: str):
        """Navigate to the home page."""
        self.open(base_url)

    def click_login(self):
        """Click the 'Log in' link exposed on the homepage."""
        self.click(self.LOGIN_LINK)
