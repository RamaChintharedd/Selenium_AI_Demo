from selenium.webdriver.common.by import By
from .base_page import BasePage


class LoginPage(BasePage):
    """
    Page object for the login page.
    Encapsulates login-specific locators and actions.
    """

    EMAIL_INPUT = (By.ID, "Email")
    PASSWORD_INPUT = (By.ID, "Password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "input.button-1.login-button")
    LOGOUT_LINK = (By.LINK_TEXT, "Log out")
    ACCOUNT_LINK = (By.LINK_TEXT, "My account")
    VALIDATION_SUMMARY = (By.CSS_SELECTOR, "div.validation-summary-errors")
    FIELD_VALIDATION_ERRORS = (By.CSS_SELECTOR, "span.field-validation-error")

    def __init__(self, driver):
        super().__init__(driver)

    def load(self, url="https://demowebshop.tricentis.com/login"):
        self.driver.get(url)

    def is_email_field_present(self):
        """Return True if email input is present and visible."""
        return self.is_element_visible(*self.EMAIL_INPUT)

    def enter_email(self, email: str):
        self.input_text(*self.EMAIL_INPUT, text=email)

    def enter_password(self, password: str):
        self.input_text(*self.PASSWORD_INPUT, text=password)

    def click_login(self):
        self.click(*self.LOGIN_BUTTON)

    def is_authenticated(self):
        """Heuristic: if Log out link or My account link is visible, consider authenticated."""
        return self.is_element_visible(*self.LOGOUT_LINK) or self.is_element_visible(*self.ACCOUNT_LINK)

    def get_validation_summary_text(self):
        return self.get_element_text(*self.VALIDATION_SUMMARY)

    def get_field_validation_errors(self):
        els = self.find_all(*self.FIELD_VALIDATION_ERRORS)
        return [el.text for el in els if el.text]
