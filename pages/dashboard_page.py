from selenium.webdriver.common.by import By
from .base_page import BasePage


class DashboardPage(BasePage):
    """Page object for a generic dashboard/home page after login."""

    WELCOME_BANNER = (By.CSS_SELECTOR, "#welcome")
    PROFILE_LINK = (By.CSS_SELECTOR, "a[href*='profile']")

    def __init__(self, driver, base_url=None):
        super().__init__(driver, base_url)
        self.base_path = "/"

    def is_welcome_visible(self) -> bool:
        return self.is_displayed(self.WELCOME_BANNER)

    def go_to_profile(self):
        self.click(self.PROFILE_LINK)


__all__ = ["DashboardPage"]
