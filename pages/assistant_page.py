from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class AssistantPage:
    """
    Page Object for the Assistant Payload Inspector test page.
    Encapsulates interactions with the payload textarea, inspect button, and response area.
    """

    def __init__(self, driver: WebDriver, page_path: str):
        self.driver = driver
        # page_path should be a file:// absolute URL or http(s) URL
        self.page_path = page_path
        self._payload_locator = (By.ID, "payload")
        self._inspect_button_locator = (By.ID, "inspect")
        self._response_locator = (By.ID, "response")

    def load(self):
        """Navigate to the assistant test page."""
        self.driver.get(self.page_path)

    def set_payload(self, json_text: str):
        """Set the JSON payload into the textarea."""
        textarea = self.driver.find_element(*self._payload_locator)
        textarea.clear()
        textarea.send_keys(json_text)

    def click_inspect(self):
        """Click the Inspect button to trigger payload inspection."""
        btn = self.driver.find_element(*self._inspect_button_locator)
        btn.click()

    def get_response_text(self) -> str:
        """Return the visible response text from the assistant."""
        resp = self.driver.find_element(*self._response_locator)
        return resp.text

    def is_prompt_visible(self) -> bool:
        """Returns True if the assistant is prompting for user_stories (prompt style)."""
        resp = self.driver.find_element(*self._response_locator)
        cls = resp.get_attribute('class') or ''
        return 'prompt' in cls

    def is_ok_visible(self) -> bool:
        """Returns True if the assistant acknowledged user_stories and is proceeding."""
        resp = self.driver.find_element(*self._response_locator)
        cls = resp.get_attribute('class') or ''
        return 'ok' in cls
