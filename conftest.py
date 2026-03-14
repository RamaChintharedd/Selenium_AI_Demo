import pytest
from utils.driver_factory import DriverFactory
from utils import config

@pytest.fixture(scope="session")
def driver():
    # Create browser driver for session; adjust headless as needed
    driver = DriverFactory.create_chrome_driver(headless=True)
    driver.implicitly_wait(config.IMPLICIT_WAIT)
    yield driver
    driver.quit()
