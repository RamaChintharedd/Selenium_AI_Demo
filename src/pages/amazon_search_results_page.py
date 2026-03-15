from selenium.webdriver.common.by import By
from .base_page import BasePage


class AmazonSearchResultsPage(BasePage):
    """Page object for Amazon search results. Contains methods to validate results and apply filters/sorting.

    Note: Amazon frequently changes DOM structure; locators are written defensively and may need updates.
    """

    RESULT_ITEMS = (By.CSS_SELECTOR, 'div.s-main-slot div[data-component-type="s-search-result"]')
    RESULT_TITLE = (By.CSS_SELECTOR, 'h2 a span')
    RESULT_PRICE_WHOLE = (By.CSS_SELECTOR, 'span.a-price-whole')
    RESULT_PRICE_FRACTION = (By.CSS_SELECTOR, 'span.a-price-fraction')
    RESULT_RATING = (By.CSS_SELECTOR, 'div.a-row.a-size-small span[aria-label]')
    RESULT_IMAGE = (By.CSS_SELECTOR, 'img.s-image')
    NO_RESULTS_MESSAGE = (By.XPATH, '//div[contains(text(), "did not match any products")]')
    SUGGESTIONS_SECTION = (By.CSS_SELECTOR, 'div.suggestions')
    SORT_DROPDOWN = (By.ID, 's-result-sort-select')

    def get_result_items(self):
        return self.finds(self.RESULT_ITEMS)

    def get_item_title(self, item_element):
        try:
            return item_element.find_element(*self.RESULT_TITLE).text
        except Exception:
            return ''

    def get_item_price(self, item_element):
        try:
            whole = item_element.find_element(*self.RESULT_PRICE_WHOLE).text
            frac = item_element.find_element(*self.RESULT_PRICE_FRACTION).text
            return f"{whole}.{frac}"
        except Exception:
            return None

    def get_item_rating(self, item_element):
        try:
            return item_element.find_element(*self.RESULT_RATING).get_attribute('aria-label')
        except Exception:
            return None

    def get_item_image(self, item_element):
        try:
            return item_element.find_element(*self.RESULT_IMAGE).get_attribute('src')
        except Exception:
            return None

    def results_contain_keyword(self, keyword: str) -> bool:
        items = self.get_result_items()
        keyword_lower = keyword.lower()
        for it in items[:10]:  # inspect first N items for speed
            title = self.get_item_title(it).lower()
            if keyword_lower in title:
                return True
        return False

    def is_no_results(self) -> bool:
        return self.is_visible(self.NO_RESULTS_MESSAGE)

    def suggestions_visible_and_clickable(self) -> bool:
        try:
            suggestions = self.find(self.SUGGESTIONS_SECTION)
            return suggestions.is_displayed()
        except Exception:
            return False

    def apply_sort(self, option_text: str):
        # Select using visible text; use JavaScript fallback if necessary
        select = self.find(self.SORT_DROPDOWN)
        try:
            from selenium.webdriver.support.select import Select

            s = Select(select)
            s.select_by_visible_text(option_text)
        except Exception:
            # Try clicking an option in a custom dropdown
            select.click()
            dropdown_option = (By.XPATH, f"//a[contains(normalize-space(.), '{option_text}')]")
            self.click(dropdown_option)

    def apply_brand_filter(self, brand_name: str):
        # Brands are often in the left facet; match by link text
        brand_locator = (By.XPATH, f"//span[text()='{brand_name}']/preceding-sibling::div//i | //a[normalize-space()='{brand_name}']")
        try:
            self.click(brand_locator)
        except Exception:
            # try partial match
            partial = (By.XPATH, f"//label[contains(., '{brand_name}')]//input")
            self.click(partial)

    def apply_price_filter(self, low: int, high: int):
        # If Amazon provides min/max inputs
        min_input = (By.ID, 'low-price')
        max_input = (By.ID, 'high-price')
        go_btn = (By.XPATH, "//input[@aria-labelledby='a-autoid-1-announce' or @type='submit']")
        try:
            self.type(min_input, str(low))
            self.type(max_input, str(high))
            self.click(go_btn)
        except Exception:
            # Fallback: click known price range link
            rng = f"${low} - ${high}"
            rng_locator = (By.LINK_TEXT, rng)
            self.click(rng_locator)
