import pytest
from utils.driver_factory import DriverFactory
from utils.config import BASE_URL
from selenium.webdriver.remote.webdriver import WebDriver
from typing import Generator


@pytest.fixture(scope="function")
def driver() -> Generator[WebDriver, None, None]:
    """
    Pytest fixture to provide a WebDriver instance to tests.
    Creates a driver, yields it to the test, and ensures proper teardown.
    """
    driver = DriverFactory.create_driver(headless=False)
    try:
        yield driver
    finally:
        driver.quit()


@pytest.fixture(scope="function")
def base_url() -> str:
    return BASE_URL
