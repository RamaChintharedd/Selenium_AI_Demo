from selenium.webdriver.common.by import By
from .base_page import BasePage


class LoginPage(BasePage):
    """
    Page object for the login page.
    Encapsulates actions and element checks for login-related scenarios.
    """

    URL = "https://demowebshop.tricentis.com/login"

    # Locators
    EMAIL_INPUT = (By.ID, "Email")
    PASSWORD_INPUT = (By.ID, "Password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "input.button-1.login-button")

    # Demo Web Shop displays some errors in div.message-error and field validation spans
    AUTH_ERROR = (By.CSS_SELECTOR, "div.message-error")
    FIELD_VALIDATION_ERRORS = (By.CSS_SELECTOR, "span.field-validation-error")

    def go_to_login_page(self):
        self.visit(self.URL)

    def is_displayed(self):
        """Check if login page is displayed by verifying presence of key controls."""
        return (
            self.is_element_present(*self.EMAIL_INPUT, visible=True)
            and self.is_element_present(*self.PASSWORD_INPUT, visible=True)
            and self.is_element_present(*self.LOGIN_BUTTON, visible=True)
        )

    def enter_email(self, email):
        self.type(*self.EMAIL_INPUT, text=email)

    def enter_password(self, password):
        self.type(*self.PASSWORD_INPUT, text=password)

    def clear_email(self):
        el = self.find(*self.EMAIL_INPUT)
        el.clear()

    def clear_password(self):
        el = self.find(*self.PASSWORD_INPUT)
        el.clear()

    def click_login(self):
        self.click(*self.LOGIN_BUTTON)

    def get_auth_error_text(self):
        if self.is_element_present(*self.AUTH_ERROR, visible=True):
            return self.get_text(*self.AUTH_ERROR)
        return ""

    def get_field_validation_texts(self):
        """Return list of field validation error texts present on the page."""
        texts = []
        try:
            elements = self.driver.find_elements(*self.FIELD_VALIDATION_ERRORS)
            for e in elements:
                text = e.text.strip()
                if text:
                    texts.append(text)
        except Exception:
            pass
        return texts

    def is_email_enabled(self):
        el = self.find(*self.EMAIL_INPUT)
        return el.is_enabled()

    def is_password_enabled(self):
        el = self.find(*self.PASSWORD_INPUT)
        return el.is_enabled()
