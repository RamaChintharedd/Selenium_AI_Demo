from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.common.exceptions import NoSuchElementException
from typing import List


class LoginPage(BasePage):
    """
    Page object for the login page. Encapsulates all interactions and query methods.
    """
    EMAIL_INPUT = (By.ID, 'Email')
    PASSWORD_INPUT = (By.ID, 'Password')
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'input.button-1.login-button')
    # Logout link used to detect authentication
    LOGOUT_LINK = (By.LINK_TEXT, 'Log out')
    # Validation summary (server-side/authentication errors)
    VALIDATION_SUMMARY = (By.CSS_SELECTOR, 'div.message-error.validation-summary-errors')
    # Field-specific validation messages
    FIELD_VALIDATIONS = (By.CSS_SELECTOR, 'span.field-validation-error')

    def __init__(self, driver):
        super().__init__(driver)

    def open(self, login_url: str):
        self.open_url(login_url)

    def enter_email(self, email: str) -> None:
        elem = self.find(self.EMAIL_INPUT)
        if elem is None:
            raise Exception('Email input not found on login page')
        elem.clear()
        elem.send_keys(email)

    def enter_password(self, password: str) -> None:
        elem = self.find(self.PASSWORD_INPUT)
        if elem is None:
            raise Exception('Password input not found on login page')
        elem.clear()
        elem.send_keys(password)

    def click_login_button(self) -> None:
        if not self.click(self.LOGIN_BUTTON):
            raise Exception('Login button not found or not clickable')

    def is_on_login_page(self) -> bool:
        return '/login' in self.get_current_url()

    def is_authenticated(self) -> bool:
        el = self.find(self.LOGOUT_LINK, timeout=3)
        return el is not None

    def get_validation_summary_text(self) -> str:
        return self.get_text(self.VALIDATION_SUMMARY)

    def get_field_validation_texts(self) -> List[str]:
        try:
            elements = self.driver.find_elements(*self.FIELD_VALIDATIONS)
            return [e.text.strip() for e in elements if e.text.strip()]
        except NoSuchElementException:
            return []

    def get_all_validation_texts(self) -> List[str]:
        texts = []
        summary = self.get_validation_summary_text()
        if summary:
            texts.append(summary)
        texts.extend(self.get_field_validation_texts())
        return texts
