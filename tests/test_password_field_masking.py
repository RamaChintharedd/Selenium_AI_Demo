from project.pages.login_page import LoginPage

from project.pages.login_page import LoginPage


def test_password_field_masking(driver, home_page):
    """Password input element should be of type 'password' and input should be masked."""
    home_page.navigate_to_login()
    login_page = LoginPage(driver)

    assert login_page.is_password_field_present_and_masked(), "Password field is not of type 'password'"

    # Optional: type and assert attribute remains 'password' (visual masking can't be programmatically asserted)
    login_page.login(email="", password="Secret123", remember=False)
    el = login_page.find(login_page.PASSWORD_INPUT)
    assert el.get_attribute("type") == "password"
