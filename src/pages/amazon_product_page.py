from selenium.webdriver.common.by import By
from .base_page import BasePage


class AmazonProductPage(BasePage):
    """Product detail page interactions: selecting options and adding to cart."""

    ADD_TO_CART_BTN = (By.ID, 'add-to-cart-button')
    SELECT_SIZE = (By.CSS_SELECTOR, 'select#native_dropdown_selected_size_name')
    SELECT_COLOR = (By.CSS_SELECTOR, 'div#variation_color_name')
    CART_COUNT = (By.ID, 'nav-cart-count')

    def select_size_if_present(self, size_text: str = None):
        try:
            select = self.find(self.SELECT_SIZE)
            if size_text:
                from selenium.webdriver.support.select import Select

                Select(select).select_by_visible_text(size_text)
            return True
        except Exception:
            return False

    def select_color_if_present(self):
        try:
            # click first color swatch
            swatch = self.find(self.SELECT_COLOR)
            swatch.click()
            return True
        except Exception:
            return False

    def click_add_to_cart(self):
        self.click(self.ADD_TO_CART_BTN)

    def go_to_cart(self):
        cart_count = self.find(self.CART_COUNT)
        cart_count.click()
