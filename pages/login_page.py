from selenium.webdriver.common.by import By
from .base_page import BasePage


class LoginPage(BasePage):
    """Page object for the login page.
    Encapsulates actions and verifications for login interactions.
    """

    # Locators - chosen to be robust for typical Demo Web Shop
    EMAIL_INPUT = (By.ID, "Email")
    PASSWORD_INPUT = (By.ID, "Password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "input.login-button")
    LOGIN_ERROR = (By.CSS_SELECTOR, "div.validation-summary-errors li")
    EMAIL_FIELD_CONTAINER = (By.ID, "Email")  # used for visibility checks

    def __init__(self, driver):
        super().__init__(driver)

    def is_email_field_present(self) -> bool:
        return self.is_displayed(*self.EMAIL_INPUT)

    def is_password_field_present(self) -> bool:
        return self.is_displayed(*self.PASSWORD_INPUT)

    def is_login_button_present(self) -> bool:
        return self.is_displayed(*self.LOGIN_BUTTON)

    def enter_email(self, email: str) -> None:
        self.type_text(*self.EMAIL_INPUT, text=email)

    def enter_password(self, password: str) -> None:
        self.type_text(*self.PASSWORD_INPUT, text=password)

    def click_login(self) -> None:
        self.click(*self.LOGIN_BUTTON)

    def get_login_error(self) -> str:
        if self.is_displayed(*self.LOGIN_ERROR):
            return self.get_element_text(*self.LOGIN_ERROR)
        return ""
