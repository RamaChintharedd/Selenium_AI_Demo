import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from utils.config import Config


# The tests below are mapped from the provided BDD scenarios.
# They use Page Objects and keep assertions readable and focused.


def test_navigate_to_login_from_homepage(driver):
    home = HomePage(driver)
    home.open(Config.BASE_URL)

    # When I click the "Log in" link or button
    home.go_to_login()

    login = LoginPage(driver)

    # Then I should be redirected to the login page (URL contains /login)
    assert login.wait_for_url_contains("/login"), "URL did not contain /login after navigating to Login page"

    # And I should see an email input field
    assert login.is_email_field_present(), "Email input field not present on Login page"

    # And I should see a password input field
    assert login.is_password_field_present(), "Password input field not present on Login page"

    # And I should see a "Log in" button
    assert login.is_login_button_present(), "Login button not present on Login page"


@pytest.mark.flaky(reruns=1)
def test_successful_login_with_valid_credentials(driver):
    # Given I am on the login page
    home = HomePage(driver)
    home.open(Config.BASE_URL)
    home.go_to_login()

    login = LoginPage(driver)

    # NOTE: This test assumes a registered account exists with Config.VALID_EMAIL and Config.VALID_PASSWORD.
    # In real test suites, create the user in a setup step or use a test account seeded into the test environment.

    # When I enter email and password and click login
    login.enter_email(Config.VALID_EMAIL)
    login.enter_password(Config.VALID_PASSWORD)
    login.click_login()

    dashboard = DashboardPage(driver)

    # Then I should be authenticated and redirected to a logged-in landing page
    assert dashboard.wait_for_url_contains("/"), "Did not navigate after login (URL check)"

    # And I should see account-specific UI elements such as "My account" or "Log out"
    assert dashboard.is_my_account_visible() or dashboard.is_logout_visible(), "Expected account-specific UI not visible after login"


def test_login_attempt_with_empty_email_field(driver):
    home = HomePage(driver)
    home.open(Config.BASE_URL)
    home.go_to_login()
    login = LoginPage(driver)

    # When I leave the email input field empty and enter valid password
    login.enter_email("")
    login.enter_password(Config.VALID_PASSWORD)
    login.click_login()

    # Then I should remain on the login page
    assert login.wait_for_url_contains("/login"), "Expected to remain on login page when email is empty"

    # And I should see a validation error or the field highlighted (we check for an error message)
    err = login.get_login_error()
    assert err != "", "Expected validation error when email is empty"


def test_login_attempt_with_invalid_email_format(driver):
    home = HomePage(driver)
    home.open(Config.BASE_URL)
    home.go_to_login()
    login = LoginPage(driver)

    # When I enter invalid email format and a valid password
    login.enter_email("invalid-email")
    login.enter_password(Config.VALID_PASSWORD)
    login.click_login()

    # Then I should remain on the login page
    assert login.wait_for_url_contains("/login"), "Expected to remain on login page when email format invalid"

    # And I should see a validation error indicating invalid email format
    err = login.get_login_error()
    assert err != "", "Expected validation error when email format is invalid"


def test_login_attempt_with_empty_password_field(driver):
    home = HomePage(driver)
    home.open(Config.BASE_URL)
    home.go_to_login()
    login = LoginPage(driver)

    # And I enter a valid registered email into the email field
    login.enter_email(Config.VALID_EMAIL)

    # When I leave the password field empty and click login
    login.enter_password("")
    login.click_login()

    # Then I should remain on the login page
    assert login.wait_for_url_contains("/login"), "Expected to remain on login page when password is empty"

    # And I should see a validation error indicating the password cannot be empty
    err = login.get_login_error()
    assert err != "", "Expected validation error when password is empty"


def test_login_attempt_with_incorrect_password(driver):
    home = HomePage(driver)
    home.open(Config.BASE_URL)
    home.go_to_login()
    login = LoginPage(driver)

    # Given a registered user exists with email (we assume Config.VALID_EMAIL exists)
    login.enter_email(Config.VALID_EMAIL)
    login.enter_password("incorrect-password")
    login.click_login()

    # Then authentication should fail and remain on login page
    assert login.wait_for_url_contains("/login"), "Expected to remain on login page when credentials are incorrect"

    # And I should see an error message indicating credentials are incorrect
    err = login.get_login_error()
    assert err != "", "Expected authentication failure message for incorrect credentials"
