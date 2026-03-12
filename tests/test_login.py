import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.account_page import AccountPage
from utils.config import Config


# Note: These tests map to the provided BDD scenarios. They use the Page Object Model
# for maintainability and separation of concerns. Some scenarios (like successful login)
# require an existing test account on the target application. Adjust credentials accordingly.


def test_navigate_to_login_from_homepage(driver):
    home = HomePage(driver)
    login = LoginPage(driver)

    home.go_to_homepage()
    home.click_login()

    assert login.wait_for_url(LoginPage.URL), f"Expected URL to be {LoginPage.URL}, got {driver.current_url}"
    assert login.is_displayed(), "Login page should display required elements"


def test_login_page_ui_elements_present(driver):
    login = LoginPage(driver)

    login.go_to_login_page()

    assert login.is_element_present(*LoginPage.EMAIL_INPUT, visible=True), "Email input should be visible"
    assert login.is_element_present(*LoginPage.PASSWORD_INPUT, visible=True), "Password input should be visible"
    assert login.is_element_present(*LoginPage.LOGIN_BUTTON, visible=True), "Login button should be visible"
    assert login.is_email_enabled(), "Email input should be enabled"
    assert login.is_password_enabled(), "Password input should be enabled"


def test_submit_empty_email_shows_error(driver):
    login = LoginPage(driver)

    login.go_to_login_page()
    login.clear_email()
    login.enter_password("ValidPassword123")
    login.click_login()

    # Expecting field validation errors
    validation_texts = login.get_field_validation_texts()
    assert any("email" in t.lower() or "e-mail" in t.lower() or "required" in t.lower() for t in validation_texts), (
        f"Expected an email required validation message, got: {validation_texts}"
    )
    assert login.current_url().startswith(LoginPage.URL), "Should remain on the login page"


@pytest.mark.parametrize("invalid_email", ["user", "user@", "user@domain"])
def test_invalid_email_format_shows_error(driver, invalid_email):
    login = LoginPage(driver)

    login.go_to_login_page()
    login.clear_email()
    login.enter_email(invalid_email)
    login.enter_password("ValidPassword123")
    login.click_login()

    validation_texts = login.get_field_validation_texts()
    assert any("valid" in t.lower() or "email" in t.lower() or "e-mail" in t.lower() for t in validation_texts), (
        f"Expected an email format validation message for '{invalid_email}', got: {validation_texts}"
    )
    assert login.current_url().startswith(LoginPage.URL), "Should remain on the login page"


def test_submit_empty_password_shows_error(driver):
    login = LoginPage(driver)

    login.go_to_login_page()
    login.enter_email("registered@example.com")
    login.clear_password()
    login.click_login()

    validation_texts = login.get_field_validation_texts()
    assert any("password" in t.lower() or "required" in t.lower() for t in validation_texts), (
        f"Expected a password required validation message, got: {validation_texts}"
    )
    assert login.current_url().startswith(LoginPage.URL), "Should remain on the login page"


@pytest.mark.parametrize("email,password", [
    ("registered@example.com", "WrongPass123"),
    ("unregistered@example.com", "AnyPassword123"),
])
def test_incorrect_credentials: An array of objects, each with file_path and code. - https://github.com/RamaChintharedd/Selenium_AI_Demo: The GitHub repository name or URL. - seleniumCode: The branch to push to. - code pushed successfully.: The commit message.  Your task: For each file in files: 1. Create or update the file at file_path in the specified repository and branch. 2. Commit the changes with commit_message.  Return STRICT JSON only: {   "push_results": [     {       "file_path": "",       "commit_url": "",       "status": "File pushed"     }   ] } Do not return explanations. Do not return markdown. Only JSON.
