import pytest
from pages.login_page import LoginPage


class TestLogin:
    """
    Tests for the login feature using the Page Object Model.
    Each test is small, focused and readable.
    """

    def test_successful_login_redirects_to_dashboard(self, driver, base_url):
        """
        Example positive test flow. Adjust selectors and assertions to match AUT.
        """
        login_page = LoginPage(driver)
        login_page.open(base_url)

        # NOTE: Replace with valid credentials for the AUT when available
        login_page.login("valid_user@example.com", "correct_password")

        # Example assertion - page-specific verification kept in test class
        # Replace with actual dashboard locator/URL verification
        assert "/dashboard" in driver.current_url

    def test_login_with_invalid_credentials_shows_error(self, driver, base_url):
        login_page = LoginPage(driver)
        login_page.open(base_url)

        login_page.login("invalid_user@example.com", "wrong_password")

        error = login_page.get_error_message()
        assert error != "" and "invalid" in error.lower()
