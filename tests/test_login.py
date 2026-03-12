import pytest
import os
from pages.home_page import HomePage
from pages.login_page import LoginPage


# Credentials can be provided via environment variables for security.
VALID_EMAIL = os.environ.get("TEST_VALID_EMAIL", "user@example.com")
VALID_PASSWORD = os.environ.get("TEST_VALID_PASSWORD", "P@ssw0rd")
INVALID_PASSWORD = "incorrect_password"


@pytest.mark.usefixtures("driver")
class TestLoginFlows:
    """
    Tests correspond to the BDD scenarios provided.
    Uses Page Object Model: HomePage and LoginPage.
    """

    def test_navigate_to_login_from_homepage(self, driver, base_url):
        home = HomePage(driver, base_url=base_url)
        home.load()
        # When I locate and click the "Log in" link or button
        home.click_login()

        login = LoginPage(driver)
        # Then the browser URL should be redirected to a login page that contains "/login"
        assert "/login" in login.get_current_url(), "Expected '/login' in URL after clicking Log in"
        # And the login page should display an email input field
        assert login.is_email_field_present(), "Email input should be visible on the login page"

    def test_successful_login_with_valid_email_and_password(self, driver):
        login = LoginPage(driver)
        login.load()

        # Given I have a registered email and the correct password
        login.enter_email(VALID_EMAIL)
        login.enter_password(VALID_PASSWORD)
        login.click_login()

        # Then I should be authenticated
        assert login.is_authenticated(), "User should be authenticated and see account-specific elements"
        # And I should be redirected to my account dashboard (heuristic: no /login in URL)
        assert "/login" not in login.get_current_url(), "Expected to be redirected away from /login after successful login"

    def test_login_attempt_with_empty_email_field(self, driver):
        login = LoginPage(driver)
        login.load()

        # Ensure email is empty and provide a valid password
        login.enter_email("")
        login.enter_password(VALID_PASSWORD)
        login.click_login()

        # Then the login should not be performed and validation shown
        assert not login.is_authenticated(), "Authentication must not occur when email is empty"
        # Prefer checking for field-level errors or validation summary
        summary = login.get_validation_summary_text()
        field_errors = login.get_field_validation_errors()
        assert summary or field_errors, "Expected a validation error when email is empty"
        # And remain on login page
        assert "/login" in login.get_current_url(), "Should remain on login page after invalid submit"

    def test_login_attempt_with_invalid_email_format(self, driver):
        login = LoginPage(driver)
        login.load()

        login.enter_email("invalidemail")
        login.enter_password(VALID_PASSWORD)
        login.click_login()

        assert not login.is_authenticated(), "Authentication must not occur with invalid email format"
        summary = login.get_validation_summary_text()
        field_errors = login.get_field_validation_errors()
        # Expect either field-level format error or a summary message
        assert summary or any("email" in e.lower() or "valid" in e.lower() for e in field_errors), \
            "Expected an email format validation message"
        assert "/login" in login.get_current_url(), "Should remain on login page after invalid submit"

    def test_login_attempt_with_empty_password_field(self, driver):
        login = LoginPage(driver)
        login.load()

        login.enter_email(VALID_EMAIL)
        login.enter_password("")
        login.click_login()

        assert not login.is_authenticated(), "Authentication must not occur when password is empty"
        summary = login.get_validation_summary_text()
        field_errors = login.get_field_validation_errors()
        assert summary or field_errors, "Expected a validation error when password is empty"
        assert "/login" in login.get_current_url(), "Should remain on login page after invalid submit"

    def test_login_attempt_with_incorrect_password(self, driver):
        login = LoginPage(driver)
        login.load()

        login.enter_email(VALID_EMAIL)
        login.enter_password(INVALID_PASSWORD)
        login.click_login()

        # Authentication should fail and an error message should be displayed
        assert not login.is_authenticated(), "Authentication must fail with incorrect password"
        summary = login.get_validation_summary_text()
        assert summary and len(summary) > 0, "Expected a validation summary indicating invalid credentials"
        assert "/login" in login.get_current_url(), "Should remain on login page after failed authentication"
