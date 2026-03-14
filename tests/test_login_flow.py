import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from utils.config import BASE_URL, REGISTERED_EMAIL, REGISTERED_PASSWORD


# Tests mapping to the provided BDD features. These use the POM defined in pages/.


def test_navigate_to_login_from_homepage(home_page: HomePage):
    """Scenario: Click 'Log in' on homepage redirects to login page"""
    login_page = home_page.click_login()
    assert login_page.is_displayed(), "Login page should be displayed after clicking Log in"
    assert login_page.get_current_url().endswith("/login"), "URL should end with /login"


def test_login_page_contains_email_input(home_page: HomePage):
    """Scenario: Verify presence of email input field on login page"""
    login_page = home_page.click_login()
    # The Email input is identified by id 'Email' on demowebshop
    assert login_page.is_displayed(), "Login page must be displayed"
    assert login_page.is_element_present(login_page.EMAIL_BY, login_page.EMAIL), "Email input should be present"


def test_successful_login_with_valid_credentials(driver):
    """Scenario: Registered user logs in successfully with valid email and password

    Note: This test requires valid credentials. Configure REGISTERED_EMAIL and REGISTERED_PASSWORD
    through utils/config.py or environment/CI secrets.
    """
    login_page = LoginPage(driver)
    login_page.open(BASE_URL)
    assert login_page.is_displayed(), "Login page must be visible"

    login_page.enter_email(REGISTERED_EMAIL)
    login_page.enter_password(REGISTERED_PASSWORD)
    login_page.click_login()

    # After clicking, the page may redirect; check authentication heuristics
    assert login_page.is_authenticated(), "User should appear authenticated (Log out or account link present)"


def test_login_with_empty_email(driver):
    """Scenario: Attempt to log in with the email field empty"""
    login = LoginPage(driver)
    login.open(BASE_URL)
    assert login.is_displayed()
    # Leave email empty
    login.enter_email("")
    login.enter_password("someValidPassword")
    login.click_login()

    # Expect validation message and remain on login page
    errors = login.get_validation_errors()
    assert errors != "", f"Expected validation errors but found none. Got: '{errors}'"
    assert login.get_current_url().endswith("/login")


def test_login_with_invalid_email_format(driver):
    """Scenario: Entering invalid email formats shows validation error"""
    login = LoginPage(driver)
    login.open(BASE_URL)
    login.enter_email("useratexample")
    login.enter_password("somePassword")
    login.click_login()

    errors = login.get_validation_errors()
    # There should be validation text; message text may vary depending on client/server validation
    assert errors != "", "Expected invalid email format validation message"
    assert login.get_current_url().endswith("/login")


def test_login_with_empty_password(driver):
    """Scenario: Attempt to log in with the password field empty"""
    login = LoginPage(driver)
    login.open(BASE_URL)
    login.enter_email(REGISTERED_EMAIL)
    login.enter_password("")
    login.click_login()

    errors = login.get_validation_errors()
    assert errors != "", "Expected validation error for empty password"
    assert login.get_current_url().endswith("/login")


def test_login_with_incorrect_password(driver):
    """Scenario: Valid email with incorrect password results in authentication failure"""
    login = LoginPage(driver)
    login.open(BASE_URL)
    login.enter_email(REGISTERED_EMAIL)
    login.enter_password("incorrect_password")
    login.click_login()

    errors = login.get_validation_errors()
    # Some sites render a specific "login was unsuccessful" message on auth failure
    assert errors != "", "Expected authentication failure message"
