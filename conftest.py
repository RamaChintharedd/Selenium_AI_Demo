import os
import pytest
from utils.driver_factory import create_chrome_driver
from pages.home_page import HomePage
from pages.login_page import LoginPage


@pytest.fixture(scope="session")
def driver():
    """Create a single WebDriver instance per test session. Quits when done."""
    headless = os.getenv("HEADLESS", "false").lower() in ("1", "true", "yes")
    driver = create_chrome_driver(headless=headless, implicit_wait=1)
    yield driver
    driver.quit()


@pytest.fixture()
def home_page(driver):
    return HomePage(driver)


@pytest.fixture()
def login_page(driver):
    return LoginPage(driver)
