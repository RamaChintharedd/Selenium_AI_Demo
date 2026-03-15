from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HomePage(BasePage):
    """
    Page object for the Demo Web Shop homepage.
    Encapsulates homepage-specific locators and actions.
    """

    URL = "https://demowebshop.tricentis.com"

    # Locators
    LOGIN_LINK = (By.LINK_TEXT, "Log in")
    # fallback locator
    LOGIN_ICON = (By.CLASS_NAME, "ico-login")

    def open(self) -> None:
        """Open the homepage."""
        self.open_url(self.URL)

    def go_to_login(self) -> None:
        """Navigate to login page by clicking the login link/icon.
        Tries a visible link first, then icon as fallback.
        """
        # Prefer visible 'Log in' link text
        if self.is_element_visible(self.LOGIN_LINK):
            self.click(self.LOGIN_LINK)
            return

        # fallback to login icon
        if self.is_element_visible(self.LOGIN_ICON):
            self.click(self.LOGIN_ICON)
            return

        raise Exception("Login link or icon was not found on the homepage")
