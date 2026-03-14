from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class DashboardPage(BasePage):
    MY_ACCOUNT_LINK = (By.LINK_TEXT, "My account")
    ORDER_HISTORY_LINK = (By.LINK_TEXT, "Orders")
    LOGOUT_LINK = (By.CLASS_NAME, "ico-logout")

    def __init__(self, driver):
        super().__init__(driver)

    def is_at_dashboard(self) -> bool:
        # On this demo site, presence of My account and Logout usually indicates an authenticated state
        return self.is_element_visible(self.MY_ACCOUNT_LINK) and self.is_element_visible(self.LOGOUT_LINK)

    def has_order_history_link(self) -> bool:
        return self.is_element_visible(self.ORDER_HISTORY_LINK)
