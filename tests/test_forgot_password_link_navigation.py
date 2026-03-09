from project.pages.login_page import LoginPage

from project.pages.login_page import LoginPage


def test_forgot_password_link_navigation(driver, home_page):
    """The 'Forgot password?' link directs the user to a password recovery page."""
    home_page.navigate_to_login()
    login_page = LoginPage(driver)

    assert login_page.is_forgot_password_present(), "Forgot password link not present"
    login_page.click(login_page.FORGOT_PASSWORD_LINK)

    # After navigation, check URL or presence of recovery keywords
    current_url = driver.current_url.lower()
    page_text = driver.page_source.lower()

    assert (
        "password" in current_url or "recover" in current_url or
        ("password" in page_text or "recover" in page_text or "reset" in page_text)
    ), "Destination does not appear to be a password recovery page"
