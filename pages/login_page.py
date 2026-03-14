from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys

class LoginPage(BasePage):
    # Locators
    EMAIL_INPUT = (By.ID, "Email")
    PASSWORD_INPUT = (By.ID, "Password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "input.login-button[type='submit'], button.login-button")
    VALIDATION_SUMMARY = (By.CSS_SELECTOR, "div.message-error.validation-summary-errors")

    def __init__(self, driver):
        super().__init__(driver)

    def is_at_login_page(self) -> bool:
        return self.current_url_contains("/login")

    def enter_email(self, email: str):
        self.type(self.EMAIL_INPUT, email)

    def enter_password(self, password: str):
        self.type(self.PASSWORD_INPUT, password)

    def click_login(self):
        self.click(self.LOGIN_BUTTON)

    def email_validation_message(self):
        """Return HTML5 built-in validation message if present or empty string otherwise."""
        try:
            el = self.find(self.EMAIL_INPUT)
            return el.get_attribute("validationMessage") or ""
        except Exception:
            return ""

    def password_validation_message(self):
        try:
            el = self.find(self.PASSWORD_INPUT)
            return el.get_attribute("validationMessage") or ""
        except Exception:
            return ""

    def has_error_summary(self) -> bool:
        return self.is_element_visible(self.VALIDATION_SUMMARY)

    def get_error_summary_text(self) -> str:
        try:
            el = self.find(self.VALIDATION_SUMMARY)
            return el.text.strip()
        except Exception:
            return ""
