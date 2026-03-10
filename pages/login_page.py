from selenium.webdriver.common.by import By
from .base_page import BasePage


class LoginPage(BasePage):
    """Page object for the login page.

    Contains only behaviors related to login (Single Responsibility).
    """

    # Locators
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    SUBMIT = (By.CSS_SELECTOR, "button[type='submit']")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".error")

    def __init__(self, driver, base_url=None):
        super().__init__(driver, base_url)
        self.base_path = "/login"

    def open(self):
        super().open(self.base_path)

    def login(self, username: str, password: str) -> None:
        """Perform login action. Returns nothing; navigation/actions are the caller's responsibility."""
        self.type(self.USERNAME, username)
        self.type(self.PASSWORD, password)
        self.click(self.SUBMIT)

    def get_error_message(self) -> str:
        return self.get_text(self.ERROR_MESSAGE)


__all__ = ["LoginPage"]
