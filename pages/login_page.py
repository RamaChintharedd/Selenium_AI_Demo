from selenium.webdriver.common.by import By
from .base_page import BasePage
from selenium.common.exceptions import TimeoutException


class LoginPage(BasePage):
    """Page object for the login page."""

    # Locators (based on demowebshop implementation)
    EMAIL_BY = By.ID
    EMAIL = "Email"
    PASSWORD_BY = By.ID
    PASSWORD = "Password"
    LOGIN_BUTTON_BY = By.CSS_SELECTOR
    LOGIN_BUTTON = "input.button-1.login-button"
    VALIDATION_SUMMARY_BY = By.CSS_SELECTOR
    VALIDATION_SUMMARY = "div.validation-summary-errors"
    LOGIN_FORM_BY = By.CSS_SELECTOR
    LOGIN_FORM = "form[action='/login']"
    LOGOUT_LINK_BY = By.LINK_TEXT
    LOGOUT_LINK = "Log out"
    # Some pages show account link or greetings; provide tolerant check
    ACCOUNT_LINK_BY = By.CSS_SELECTOR
    ACCOUNT_LINK = "a.account"

    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)

    def open(self, base_url: str):
        """Navigate directly to the login page."""
        self.go_to(f"{base_url}/login")

    def is_displayed(self) -> bool:
        """Check that login form is visible on the page."""
        return self.is_element_present(self.LOGIN_FORM_BY, self.LOGIN_FORM, timeout=5)

    def enter_email(self, email: str):
        self.type(self.EMAIL_BY, self.EMAIL, email)

    def enter_password(self, password: str):
        self.type(self.PASSWORD_BY, self.PASSWORD, password)

    def click_login(self):
        self.click(self.LOGIN_BUTTON_BY, self.LOGIN_BUTTON)

    def get_validation_errors(self) -> str:
        """Return validation summary text if present."""
        el = self.find_optional(self.VALIDATION_SUMMARY_BY, self.VALIDATION_SUMMARY, timeout=2)
        return el.text.strip() if el else ""

    def is_authenticated(self) -> bool:
        """Determine if the user appears authenticated by checking for account-specific elements.

        This uses presence of "Log out" or an account link as a heuristic.
        """
        if self.is_element_present(self.LOGOUT_LINK_BY, self.LOGOUT_LINK, timeout=2):
            return True
        if self.is_element_present(self.ACCOUNT_LINK_BY, self.ACCOUNT_LINK, timeout=2):
            return True
        return False

    def get_current_url(self) -> str:
        return super().get_current_url()
