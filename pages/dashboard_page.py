from selenium.webdriver.common.by import By
from .base_page import BasePage


class DashboardPage(BasePage):
    """Page object for the logged-in landing/dashboard page.
    Contains checks for account-specific UI elements.
    """

    MY_ACCOUNT_LINK = (By.LINK_TEXT, "My account")
    LOGOUT_LINK = (By.LINK_TEXT, "Log out")

    def __init__(self, driver):
        super().__init__(driver)

    def is_my_account_visible(self) -> bool:
        return self.is_displayed(*self.MY_ACCOUNT_LINK)

    def is_logout_visible(self) -> bool:
        return self.is_displayed(*self.LOGOUT_LINK)
