from selenium.webdriver.common.by import By
from .base_page import BasePage


class AmazonCartPage(BasePage):
    """Cart page object for verifying cart contents and updating quantities."""

    CART_ITEMS = (By.CSS_SELECTOR, 'div.sc-list-item')
    ITEM_TITLE = (By.CSS_SELECTOR, 'span.a-list-item a.sc-product-link')
    ITEM_PRICE = (By.CSS_SELECTOR, 'span.sc-product-price')
    ITEM_QUANTITY = (By.CSS_SELECTOR, 'select.sc-update-quantity-input')
    SUBTOTAL = (By.ID, 'sc-subtotal-amount-activecart')

    def get_cart_items(self):
        return self.finds(self.CART_ITEMS)

    def find_item_by_title(self, title_substring: str):
        for it in self.get_cart_items():
            try:
                title = it.find_element(*self.ITEM_TITLE).text
                if title_substring.lower() in title.lower():
                    return it
            except Exception:
                continue
        return None

    def get_item_price(self, item_element):
        try:
            price_text = item_element.find_element(*self.ITEM_PRICE).text
            # Normalize price like "$12.34" -> 12.34
            return float(price_text.replace('$', '').replace(',', '').strip())
        except Exception:
            return None

    def get_item_quantity(self, item_element):
        try:
            select = item_element.find_element(*self.ITEM_QUANTITY)
            return select.get_attribute('value')
        except Exception:
            return None

    def update_item_quantity(self, item_element, quantity: int):
        try:
            from selenium.webdriver.support.select import Select

            select = Select(item_element.find_element(*self.ITEM_QUANTITY))
            select.select_by_value(str(quantity))
            return True
        except Exception:
            return False

    def get_subtotal(self):
        try:
            return self.find(self.SUBTOTAL).text
        except Exception:
            return None
