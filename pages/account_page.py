from selenium.webdriver.common.by import By
from .base_page import BasePage


class AccountPage(BasePage):
    """
    Page object for account-specific areas post-login.
    """

    MY_ACCOUNT_LINK = (By.LINK_TEXT, "My account")
    LOGOUT_LINK = (By.LINK_TEXT, "Log out")
    ORDER_HISTORY_LINK = (By.LINK_TEXT, "Orders")

    def is_account_menu_visible(self):
        return self.is_element_present(*self.MY_ACCOUNT_LINK, visible=True)

    def is_logout_visible(self):
        return self.is_element_present(*self.LOGOUT_LINK, visible=True)

    def go_to_order_history(self):
        if self.is_element_present(*self.ORDER_HISTORY_LINK, visible=True):
            self.click(*self.ORDER_HISTORY_LINK)
            return True
        return False
