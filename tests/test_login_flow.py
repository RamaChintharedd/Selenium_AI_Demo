import time
import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from config import BASE_URL, LOGIN_URL, REGISTERED_EMAIL, REGISTERED_PASSWORD


# Note: Tests rely on environment-provided credentials for the "successful login" scenario.
# Set REGISTERED_EMAIL and REGISTERED_PASSWORD environment variables before running tests.


def test_navigate_to_login_from_homepage(driver):
    home = HomePage(driver)
    login = LoginPage(driver)

    home.open(BASE_URL)
    home.click_login()

    assert '/login' in driver.current_url, "Expected to be redirected to a URL containing '/login'"
    # Check presence of essential login form elements
    assert login.find(login.EMAIL_INPUT) is not None, "Email input should be visible on login page"
    assert login.find(login.PASSWORD_INPUT) is not None, "Password input should be visible on login page"
    assert login.find(login.LOGIN_BUTTON) is not None, "Log in button should be visible on login page"


@pytest.mark.skipif(REGISTERED_PASSWORD == 'replace_with_valid_password', reason='No real password provided via env')
def test_successful_login_with_valid_credentials(driver):
    login = LoginPage(driver)
    login.open(LOGIN_URL)

    login.enter_email(REGISTERED_EMAIL)
    login.enter_password(REGISTERED_PASSWORD)
    login.click_login_button()

    # Allow time for redirect/login processing
    time.sleep(1)

    assert not login.is_on_login_page(), "After successful login we should not remain on the login page"
    assert login.is_authenticated(), "Log out link should be present to indicate authentication"


def test_login_with_empty_email_field(driver):
    login = LoginPage(driver)
    login.open(LOGIN_URL)

    # Leave email empty
    login.enter_email('')
    login.enter_password('anyPassword123')
    login.click_login_button()

    assert login.is_on_login_page(), "Should remain on login page when email is empty"
    validations = login.get_all_validation_texts()
    assert any(validations), "Expected at least one validation or error message when email is empty"
    assert not login.is_authenticated(), "Should not be authenticated when email is empty"


def test_login_with_invalid_email_format(driver):
    login = LoginPage(driver)
    login.open(LOGIN_URL)

    login.enter_email('invalid-email')
    login.enter_password('anyPassword123')
    login.click_login_button()

    assert login.is_on_login_page(), "Should remain on login page when email format is invalid"
    validations = login.get_all_validation_texts()
    assert any('email' in v.lower() or 'invalid' in v.lower() for v in validations) or any(validations), \
        "Expected a validation message indicating invalid email format"
    assert not login.is_authenticated(), "Should not be authenticated with invalid email format"


def test_login_with_empty_password_field(driver):
    login = LoginPage(driver)
    login.open(LOGIN_URL)

    # Use a registered email if available, otherwise a placeholder
    email = REGISTERED_EMAIL
    login.enter_email(email)
    login.enter_password('')
    login.click_login_button()

    assert login.is_on_login_page(), "Should remain on login page when password is empty"
    validations = login.get_all_validation_texts()
    assert any(validations), "Expected a validation or error message indicating password cannot be empty"
    assert not login.is_authenticated(), "Should not be authenticated when password is empty"


def test_login_with_incorrect_credentials(driver):
    login = LoginPage(driver)
    login.open(LOGIN_URL)

    # Use a registered email if possible, otherwise a likely-registered placeholder
    email = REGISTERED_EMAIL
    login.enter_email(email)
    login.enter_password('incorrectPassword!')
    login.click_login_button()

    assert login.is_on_login_page(), "Should remain on login page with incorrect credentials"
    validations = login.get_all_validation_texts()
    # Authentication errors typically appear in validation summary
    assert any(validations), "Expected an authentication error message for incorrect credentials"
    assert not login.is_authenticated(), "Should not be authenticated with incorrect credentials"


def test_email_field_client_side_validation_behaviors(driver):
    login = LoginPage(driver)
    login.open(LOGIN_URL)

    # 1) Whitespace-only email
    login.enter_email('   ')
    login.enter_password('anyPassword123')
    login.click_login_button()

    assert login.is_on_login_page(), "Whitespace-only email should be treated as empty and remain on login page"
    validations_ws = login.get_all_validation_texts()
    assert any(validations_ws), "Expected validation message when email is whitespace-only"
    assert not login.is_authenticated()

    # 2) Leading/trailing whitespace should be trimmed before validation/authentication
    login.open(LOGIN_URL)
    login.enter_email('  ' + REGISTERED_EMAIL + '  ')
    login.enter_password(REGISTERED_PASSWORD if REGISTERED_PASSWORD != 'replace_with_valid_password' else 'invalid-temp')
    login.click_login_button()

    # If real credentials were supplied via env, expect authentication. Otherwise, remain on login page.
    if REGISTERED_PASSWORD != 'replace_with_valid_password':
        assert login.is_authenticated(), "Trimmed credentials should authenticate if valid"
    else:
        # Without a real password, we expect not authenticated; but the: An array of objects, each with file_path and code. - https://github.com/RamaChintharedd/Selenium_AI_Demo: The GitHub repository name or URL. - seleniumCode: The branch to push to. - code pushed successfully.: The commit message.  Your task: For each file in files: 1. Create or update the file at file_path in the specified repository and branch. 2. Commit the changes with commit_message.  Return STRICT JSON only: {   "push_results": [     {       "file_path": "",       "commit_url": "",       "status": "File pushed"     }   ] } Do not return explanations. Do not return markdown. Only JSON.
