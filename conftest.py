import pytest
from utils.driver_factory import create_chrome_driver
from utils.config import BASE_URL, DEFAULT_TIMEOUT
from pages.home_page import HomePage
from pages.login_page import LoginPage
import os


def pytest_addoption(parser):
    parser.addoption("--headless", action="store_true", default=False, help="Run browsers headless")


@pytest.fixture(scope="session")
def base_url():
    return BASE_URL


@pytest.fixture(scope="function")
def driver(request, pytestconfig):
    """Create a WebDriver and quit after test. Default Chrome."""
    headless = pytestconfig.getoption("--headless")
    driver = create_chrome_driver(headless=headless)
    driver.maximize_window()
    yield driver
    try:
        driver.quit()
    except Exception:
        pass


@pytest.fixture
def home_page(driver, base_url):
    page = HomePage(driver, timeout=DEFAULT_TIMEOUT)
    page.open(base_url)
    return page


@pytest.fixture
def login_page(driver, base_url):
    page = LoginPage(driver, timeout=DEFAULT_TIMEOUT)
    page.open(base_url)
    return page
