from selenium.webdriver.common.by import By
from .base_page import BasePage
from pages.login_page import LoginPage


class HomePage(BasePage):
    """Page object for Demo Web Shop homepage."""

    # Locators
    LOGIN_LINK_BY = By.LINK_TEXT
    LOGIN_LINK = "Log in"
    # alternative locator: top link with class 'ico-login'
    LOGIN_ICON_BY = By.CSS_SELECTOR
    LOGIN_ICON = "a.ico-login"

    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)

    def open(self, base_url: str):
        """Open the homepage."""
        self.go_to(base_url)

    def click_login(self) -> LoginPage:
        """Click the login link/icon and return login page object.

        Uses multiple locator strategies for robustness.
        """
        # Prefer visible link text, fallback to icon
        if self.is_element_present(self.LOGIN_LINK_BY, self.LOGIN_LINK, timeout=2):
            self.click(self.LOGIN_LINK_BY, self.LOGIN_LINK)
        else:
            self.click(self.LOGIN_ICON_BY, self.LOGIN_ICON)
        return LoginPage(self.driver, timeout=self.timeout)
