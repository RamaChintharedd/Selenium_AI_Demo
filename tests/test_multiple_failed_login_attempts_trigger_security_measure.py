from project.pages.login_page import LoginPage

from project.pages.login_page import LoginPage
import os


def test_multiple_failed_login_attempts_trigger_security_measure(driver, home_page):
    """Repeated failed login attempts trigger a security mechanism such as CAPTCHA or lockout."""
    home_page.navigate_to_login()
    login_page = LoginPage(driver)

    email = os.getenv("TEST_USER_EMAIL")
    if not email:
        # Use a plausible registered-email; if not available treat as unregistered flow
        email = "test@example.com"

    failed_password = "WrongPass!"
    max_attempts = 8
    security_triggered = False

    for attempt in range(max_attempts):
        login_page.login(email=email, password=failed_password, remember=False)
        # Short pause between attempts could be necessary for server-side counters
        import time
        time.sleep(1)

        # Check for presence of any obvious security measure indicators
        generic_error = login_page.get_generic_error().lower()
        page_source = driver.page_source.lower()

        # Heuristic checks: presence of captcha, lockout, too many attempts
        if ("captcha" in page_source) or ("too many" in generic_error) or ("locked" in generic_error) or ("temporarily" in generic_error):
            security_triggered = True
            break

    assert security_triggered, (
        "No security measure detected after multiple failed attempts. "
        "If application intentionally does not implement rate limiting/lockout, document as security gap."
    )
