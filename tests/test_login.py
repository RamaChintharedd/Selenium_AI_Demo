import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from utils import config

# Tests implemented using pytest and Page Object Model.
# Each test targets a single behavior and is readable and maintainable.

class TestLoginScenarios:
    def test_navigate_to_login_and_verify_fields(self, driver):
        home = HomePage(driver)
        login = LoginPage(driver)

        home.open_homepage(config.BASE_URL)
        home.click_login()

        assert login.is_at_login_page(), "Browser did not navigate to the login page"
        assert login.is_element_visible(LoginPage.EMAIL_INPUT), "Email input should be visible"
        assert login.is_element_visible(LoginPage.PASSWORD_INPUT), "Password input should be visible"
        assert login.is_element_visible(LoginPage.LOGIN_BUTTON), "Login button should be visible"

    def test_successful_login_with_valid_credentials(self, driver):
        home = HomePage(driver)
        login = LoginPage(driver)
        dashboard = DashboardPage(driver)

        home.open_homepage(config.BASE_URL)
        home.click_login()

        login.enter_email(config.VALID_EMAIL)
        login.enter_password(config.VALID_PASSWORD)
        login.click_login()

        # After successful login, dashboard indicators should be visible
        assert dashboard.is_at_dashboard(), "User should be authenticated and see dashboard elements"
        assert dashboard.has_order_history_link(), "Order history link should be visible after login"

    def test_submit_login_with_empty_email(self, driver):
        home = HomePage(driver)
        login = LoginPage(driver)

        home.open_homepage(config.BASE_URL)
        home.click_login()

        # Ensure email is empty and password present
        login.enter_email("")
        login.enter_password(config.VALID_PASSWORD)
        login.click_login()

        # Prefer client-side HTML5 validation message if present. Otherwise, server returns an error summary.
        email_msg = login.email_validation_message()
        if email_msg:
            assert email_msg != "", "Expected browser validation message for empty email"
            assert login.is_at_login_page(), "User should remain on the login page"
        else:
            # Fallback: server-side summary
            assert login.has_error_summary(), "Expected validation summary when submitting empty email"
            assert login.is_at_login_page(), "User should remain on the login page"

    def test_submit_login_with_invalid_email_format(self, driver):
        home = HomePage(driver)
        login = LoginPage(driver)

        home.open_homepage(config.BASE_URL)
        home.click_login()

        login.enter_email(config.INVALID_EMAIL)
        login.enter_password(config.VALID_PASSWORD)
        login.click_login()

        # If browser disallows invalid format, HTML5 validation message should appear
        email_msg = login.email_validation_message()
        if email_msg:
            assert "valid" in email_msg.lower() or "email" in email_msg.lower()
            assert login.is_at_login_page()
        else:
            # Server side: check for error summary indicating invalid credentials/format
            assert login.has_error_summary(), "Expected error summary for invalid email format"
            assert login.is_at_login_page()

    def test_submit_login_with_empty_password(self, driver):
        home = HomePage(driver)
        login = LoginPage(driver)

        home.open_homepage(config.BASE_URL)
        home.click_login()

        login.enter_email(config.VALID_EMAIL)
        login.enter_password("")
        login.click_login()

        pwd_msg = login.password_validation_message()
        if pwd_msg:
            assert pwd_msg != "", "Expected browser validation message for empty password"
            assert login.is_at_login_page()
        else:
            assert login.has_error_summary(), "Expected validation summary when submitting empty password"
            assert login.is_at_login_page()

    def test_submit_login_with_incorrect_password(self, driver):
        home = HomePage(driver)
        login = LoginPage(driver)

        home.open_homepage(config.BASE_URL)
        home.click_login()

        login.enter_email(config.VALID_EMAIL)
        login.enter_password(config.INCORRECT_PASSWORD)
        login.click_login()

        # Authentication should fail and error should be displayed
        assert login.has_error_summary(), "Expected authentication error when password is incorrect"
        summary_text = login.get_error_summary_text().lower()
        assert "login was unsuccessful" in summary_text or "unsuccessful" in summary_text or "wrong" in summary_text
        assert login.is_at_login_page()
