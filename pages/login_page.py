from selenium.webdriver.common.by import By
from .base_page import BasePage
from selenium.webdriver.remote.webdriver import WebDriver
from typing import Tuple


class LoginPage(BasePage):
    """
    Page Object representing the login page.
    Encapsulates locators and actions related to login functionality.
    """

    # Locators as class-level constants - easy to reuse and maintain
    USERNAME_INPUT: Tuple[str, str] = (By.ID, "username")
    PASSWORD_INPUT: Tuple[str, str] = (By.ID, "password")
    LOGIN_BUTTON: Tuple[str, str] = (By.ID, "login-button")
    ERROR_MESSAGE: Tuple[str, str] = (By.CSS_SELECTOR, "div.error")

    def __init__(self, driver: WebDriver, timeout: int = 10) -> None:
        super().__init__(driver, timeout)

    def open(self, base_url: str) -> None:
        self.navigate_to(base_url + "/login")

    def login(self, username: str, password: str) -> None:
        """Performs the login action. Keeps implementation details inside the page object."""
        self.enter_text(self.USERNAME_INPUT, username)
        self.enter_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def get_error_message(self) -> str:
        if self.is_element_present(self.ERROR_MESSAGE):
            return self.get_text(self.ERROR_MESSAGE)
        return ""
