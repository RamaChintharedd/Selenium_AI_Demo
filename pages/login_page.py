from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from typing import Optional


class LoginPage(BasePage):
    """
    Page object for the Login Page. Encapsulates interactions with the login form.
    """

    URL = "https://demowebshop.tricentis.com/login"

    # Locators
    EMAIL_INPUT = (By.ID, "Email")
    PASSWORD_INPUT = (By.ID, "Password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "input.button-1.login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "div.message-error.validation-summary-errors")
    MY_ACCOUNT_LINK = (By.LINK_TEXT, "My account")

    def open(self) -> None:
        self.open_url(self.URL)

    def is_email_present(self) -> bool:
        return self.is_element_visible(self.EMAIL_INPUT)

    def is_password_present(self) -> bool:
        return self.is_element_visible(self.PASSWORD_INPUT)

    def enter_email(self, email: str) -> None:
        el = self.find_visible(self.EMAIL_INPUT)
        el.clear()
        el.send_keys(email)

    def enter_password(self, password: str) -> None:
        el = self.find_visible(self.PASSWORD_INPUT)
        el.clear()
        el.send_keys(password)

    def click_login(self) -> None:
        self.click(self.LOGIN_BUTTON)

    def login(self, email: str, password: str) -> None:
        """Combines email + password entry and submits the form."""
        self.enter_email(email)
        self.enter_password(password)
        self.click_login()

    def get_error_message_text(self) -> Optional[str]:
        return self.get_text(self.ERROR_MESSAGE)

    def is_authenticated(self) -> bool:
        """Detects whether user-specific navigation exists after login.
        This checks for 'My account' link which appears for authenticated users.
        """
        return self.is_element_visible(self.MY_ACCOUNT_LINK)
