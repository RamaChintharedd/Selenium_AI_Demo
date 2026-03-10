import pytest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


@pytest.mark.smoke
def test_login_success(driver, config):
    """Example test: Verify login flows to dashboard.

    This is a sample test demonstrating POM usage. Adapt locators/URL to your application.
    """
    base_url = config.BASE_URL
    login_page = LoginPage(driver, base_url=base_url)
    dashboard_page = DashboardPage(driver, base_url=base_url)

    login_page.open()

    # NOTE: These credentials are placeholders. Replace with test credentials or secrets management.
    login_page.login("testuser", "correct_password")

    # Assert that the welcome banner is visible on the dashboard
    assert dashboard_page.is_welcome_visible(), "Welcome banner should be visible after login"


@pytest.mark.regression
def test_login_failure_shows_error(driver, config):
    base_url = config.BASE_URL
    login_page = LoginPage(driver, base_url=base_url)

    login_page.open()
    login_page.login("wrong", "credentials")

    error_text = login_page.get_error_message()
    assert "invalid" in error_text.lower() or error_text != "", "An error message should be shown for bad credentials"
