import os
import pytest
from selenium.common.exceptions import TimeoutException


# Tests corresponds to the Gherkin features provided. They use the Page Object Model.
# Some tests require real registered credentials; these are read from environment variables
# REGISTERED_EMAIL and REGISTERED_PASSWORD. If not provided, the successful-login test
# will be skipped to avoid false failures.


def test_navigate_to_login_from_homepage(home_page, login_page):
    """Feature: Navigate to Login Page from Homepage"""
    home_page.open()
    home_page.go_to_login()

    # Verify URL and that login form fields exist
    assert login_page.current_url().startswith(login_page.URL), (
        f"Expected to be on login page (starts with {login_page.URL}), got {login_page.current_url()}"
    )
    assert login_page.is_email_present(), "Email input was not displayed on login page"
    assert login_page.is_password_present(), "Password input was not displayed on login page"


def test_email_input_field_present_visible_editable(login_page):
    """Feature: Email input field is present, visible and editable"""
    login_page.open()

    assert login_page.is_email_present(), "Email input not present"

    # Try typing into the field
    test_email = "sample@example.com"
    login_page.enter_email(test_email)

    # Read back the value using JavaScript since some pages may not expose value via text
    current_value = login_page.driver.execute_script("return document.getElementById('Email').value;")
    assert current_value == test_email, f"Expected email input to contain '{test_email}', found '{current_value}'"


def test_successful_login_with_valid_credentials(login_page):
    """Feature: Successful Login with Valid Credentials
    This test requires environment variables REGISTERED_EMAIL and REGISTERED_PASSWORD.
    If not provided, the test will be skipped.
    """
    registered_email = os.getenv("REGISTERED_EMAIL")
    registered_password = os.getenv("REGISTERED_PASSWORD")

    if not registered_email or not registered_password:
        pytest.skip("REGISTERED_EMAIL and REGISTERED_PASSWORD are not set; skipping successful login test")

    login_page.open()
    login_page.login(registered_email, registered_password)

    # After login, expect to either be redirected away from /login or have an authenticated element
    try:
        assert login_page.is_authenticated(), "Authenticated navigation element not found after login"
    except TimeoutException:
        pytest.fail("Login did not result in authenticated state (timeout waiting for auth element)")


def test_validation_error_when_email_empty(login_page):
    """Feature: Validation Error when Email Field is Empty"""
    login_page.open()

    # Ensure email emptied and a password provided
    login_page.enter_email("")
    login_page.enter_password("SomePassword123")
    login_page.click_login()

    # Expect the user remains on login page and an error message is shown
    assert login_page.current_url().startswith(login_page.URL), "User should remain on login page when email is empty"
    error_text = login_page.get_error_message_text()
    assert error_text is not None and ("email" in error_text.lower() or "required" in error_text.lower() or "enter" in error_text.lower()), (
        f"Expected validation error about email being required. Got: {error_text}"
    )


def test_validation_invalid_email_format(login_page):
    """Feature: Validation Error for Invalid Email Format"""
    login_page.open()
    login_page.enter_email("invalid-email")
    login_page.enter_password("anything")
    login_page.click_login()

    assert login_page.current_url().startswith(login_page.URL), "User should remain on login page when email format is invalid"
    error_text = login_page.get_error_message_text()
    # Some implementations show inline validation or error summary; accept multiple forms
    assert error_text is not None and ("email" in error_text.lower() or "invalid" in error_text.lower() or "format" in error_text.lower()), (
        f"Expected invalid email format message. Got: {error_text}"
    )


def test_validation_password_empty(login_page):
    """Feature: Validation/Error when Password Field is Empty"""
    login_page.open()
    # Enter a plausible registered email; do not require a real registered user here. Use a sample.
    login_page.enter_email("registered_user@example.com")
    login_page.enter_password("")
    login_page.click: An array of objects, each with file_path and code. - https://github.com/RamaChintharedd/Selenium_AI_Demo: The GitHub repository name or URL. - seleniumCode: The branch to push to. - code pushed successfully.: The commit message.  Your task: For each file in files: 1. Create or update the file at file_path in the specified repository and branch. 2. Commit the changes with commit_message.  Return STRICT JSON only: {   "push_results": [     {       "file_path": "",       "commit_url": "",       "status": "File pushed"     }   ] } Do not return explanations. Do not return markdown. Only JSON.
