import pytest
from utils.driver_factory import create_chrome_driver
from config import DEFAULT_TIMEOUT


@pytest.fixture(scope='function')
def driver(request):
    """Creates a WebDriver and ensures it quits after the test."""
    headless_flag = False
    driver = create_chrome_driver(headless=headless_flag)
    yield driver
    try:
        driver.quit()
    except Exception:
        pass
